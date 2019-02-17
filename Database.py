# -*- coding: UTF-8 -*-
import pymysql,logging,os
from configparser import ConfigParser
import copy
#提供从数据库取数据的方法
class OperationDb_interface(object):

    def __init__(self,databaseName):
        cp = ConfigParser()
        cp.read("conf.ini")
        section = cp.sections()[0]
        host = cp.get(section, "host")
        user = cp.get(section, 'user')
        passwd = cp.get(section, 'passwd')
        port = cp.getint(section, 'port')
        # 初始化类
        self.conn=pymysql.connect(host=host,user=user,passwd=passwd,db=databaseName,port=port,charset='utf8')#创建数据库连接
        self.cur=self.conn.cursor(cursor=pymysql.cursors.DictCursor)#创建游标
    def op_sql(self,param):
        try:
            self.cur.execute(param)#执行sql语句
            self.conn.commit()#提交改变
            return True
        except pymysql.Error as e:
            print("Mysql Error %d:%s" %(e.args[0],e.args[1]))
            logging.basicConfig(filename=os.path.join(os.getcwd(),'./mysql_errlog.txt'),
                                level = logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
            return  False
    #查询单条数据
    def selectOne(self,condition):
        try:
            self.cur.execute(condition)
            results = self.cur.fetchone()#获取一条数据
        except pymysql.Error as e:
            results='执行sql错误'#数据库执行错误
            print("Mysql Error %d：%s" %(e.args[0],e.args[1]))
            logging.basicConfig(filename=os.path.join(os.getcwd(), './mysql_errlog.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        finally:
            return results
    #查询多条数据
    def selectAll(self,condition):
        try:
            self.cur.execute(condition)
            self.cur.scroll(0,mode='absolute')#光标回到初始位置
            results = self.cur.fetchall()#返回游标中所有结果
        except pymysql.Error as e:
            results='执行sql错误'#数据库执行错误
            print("Mysql Error %d：%s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=os.path.join(os.getcwd(), './mysql_errlog.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        finally:
            return results

    # #定义表中插入多条数据操作
    # def insertMore(self,condition,params):
    #     try:
    #         self.cur.executemany(condition,params)
    #         self.conn.commit()
    #         return True
    #     except pymysql.Error as e:
    #         print("Mysql Error %d:%s" %(e.args[0],e.args[1]))
    #         logging.basicConfig(filename=os.path.join(os.getcwd(),'./log.txt'),
    #                             level = logging.DEBUG,
    #                             format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    #         logger = logging.getLogger(__name__)
    #         logger.exception(e)
    #         return  False
    # #删除一条数据
    # def deleteOne(self, condition,params):
    #     try:
    #         self.cur.executemany(condition,params)
    #         self.conn.commit()
    #         return True
    #     except pymysql.Error as e:
    #         print("Mysql Error %d:%s" % (e.args[0], e.args[1]))
    #         logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'), level=logging.DEBUG,
    #                             format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    #         logger = logging.getLogger(__name__)
    #         logger.exception(e)
    #         return False
    #
    #  # 修改一条数据
    # def updateOne(self, condition):
    #     try:
    #         self.cur.execute(condition)
    #         self.conn.commit()
    #         return True
    #     except pymysql.Error as e:
    #         print("Mysql Error %d:%s" % (e.args[0], e.args[1]))
    #         logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'), level=logging.DEBUG,
    #                             format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    #         logger = logging.getLogger(__name__)
    #         logger.exception(e)
    #         return False


    def __del__(self):
        if self.cur !=None:
            self.cur.close()
        if self.conn!=None:
            self.conn.close()



if __name__=="__main__":


    #result = test.deleteOne("delete from student where name=%s",params=[("abcdef"),("abcde")])
    #result = test.updateOne("update student set name='abcdef' where id=1")
    #result = test.insertMore('INSERT INTO student values(8,"aaa")')
    #result = test.insertMore('INSERT INTO student values(%s,%s)',params=[(1,"ab"),(2,"abcd"),(3,"abcde")])
    li = list()
    test = OperationDb_interface('mysql157_user')  # 实例化类
    Mobile = (test.selectAll(
        "select mobile from tbsoul limit 1000000"))
    print(Mobile)
    v=[]
    [v.append(i.get('mobile')) for i  in Mobile]
    print(v)
    # mobiles = list()
    # for m in range(0, 1000000):
    #     Mobile = (test.selectAll(
    #         "select mobile from tbsoul limit 10000".format(m))).get('mobile')  # 从数据库取第一条数据
    #     mobiles.append(Mobile)  # 获取键为mobile的值
    # print(mobiles)


