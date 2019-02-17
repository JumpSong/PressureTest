# coding: utf-8
import os
import sys
import tarfile
import paramiko

def tar_files(source_dir:str, arcname=None):
    """Tar the specific dir.

    :param str source_dir:
    :param str arcname: 
    :return:
    """
    with tarfile.open('%s.tar' % source_dir, 'w') as tar:
        if arcname:
            tar.add(source_dir, arcname=arcname)
        else:
            tar.add(source_dir, arcname=os.path.basename(source_dir))

def get_ssh_client(ssh_host=None, port=22, username='root', passwd=None)->paramiko.SSHClient:
    """

    :param str ssh_host: remote host address.
    :param int port: remote host port.
    :param str username: host username.
    :param str passwd: host password.
    :return:
    """
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=ssh_host,
                           port=port,
                           username=username,
                           password=passwd)
        return ssh_client
    except:
        print('%s connect error.' % ssh_host)

def run_ssh_commands(ssh:paramiko.SSHClient, commands_list:list)->list:
    """
    :param ssh: ssh client
    :param commands_list: all commands need to run on remote host.
    :return: 
    """
    output = []
    for command in commands_list:
        stdin, stdout, stderr = ssh.exec_command(command)
        out_info = stdout.readlines()
        for info_perline in out_info:
            output.append(info_perline)
    return output

def start_deploy_service(host_addr:str,cmd_list:list,tar_src='tl',tar_dst='tl.tar'):
    tar_files(tar_src)
    ssh = get_ssh_client(ssh_host=host_addr, port=22, username='root', passwd='123456')

    print('http://' + host_addr)
    sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    sftp.put(localpath=tar_dst, remotepath=tar_dst)
    info_modify = run_ssh_commands(ssh, cmd_list)
    for info in info_modify:
        print(info)


if __name__ == '__main__':
    meta_server = os.getenv("MetaServer")
    host_addr = os.getenv('DeployServer')
    k8s_addr = os.getenv('K8sServer')
    svc = os.getenv('Service')
    print("JobName: %s" %(svc))
    if meta_server:
        meta_server = meta_server.strip('http://')
        print("MetaServer:%s" %(meta_server))
    else:
        meta_server = "192.168.1.28:8080"
        os.environ['MetaServer'] = meta_server
        print("MetaServer using default:%s" %(meta_server))

    cmd_list = ['for f in `find . -name "docker-compose.yaml"`; do echo ${f%/*} && cd ${f%/*} && docker-compose down && cd ../ ;done && wait',
                'test -d "{svc}" && cd {svc} && docker-compose down && cd ../ && rm -rf {svc}'.format(svc=svc),
                'tar -xf {svc}.tar && rm -rf {svc}.tar'.format(svc=svc),
                'cd {svc} && sed -e "s/devIP/{k8s_addr}/g" -e "s/metaIP/http:\/\/{meta_server}/g" -e "s/hostIP/{host_addr}/g" -i docker-compose.yaml'.format(svc=svc,host_addr=host_addr,k8s_addr=k8s_addr,meta_server=meta_server),
                'cd {svc} && docker-compose up -d'.format(svc=svc)]
    start_deploy_service(host_addr=host_addr,cmd_list=cmd_list,tar_src=svc,tar_dst=svc+'.tar')

