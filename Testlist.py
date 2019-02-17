# -*- coding: utf-8 -*-
import sys
import os
ROOT_PATH =  os.path.dirname(os.path.abspath("__file__"))
sys.path.append(ROOT_PATH)

from testerDatabase import *
from Business_Gateway.TeacherServer_Tests import *
from MicroService.UserServer_Tests import *
from MicroService.HomePage_Tests import *
from MicroService.ParamServer_Tests import *
from Business_Gateway.BookServer_Tests import *
from Business_Gateway.SchoolMateServer_Tests import *
from Business_Gateway.MindStreetServer_Tests import *
from Business_Gateway.RentHouseServer_Tests import *
from Business_Gateway.LeaseServer_Tests import *
from Business_Gateway.JobServer_Tests import *
from MicroService.TipServer_Tests import *
from Business_Gateway.ClubServer_Tests import *
from Business_Gateway.FigureServer_Tests import *
from Business_Gateway.LifeSupplyServer_Tests import *
from Business_Gateway.InterestServer_Tests import *
from Business_Gateway.GiftServer_Tests import *
from Business_Gateway.ConferenceServer_Tests import *
from Business_Gateway.PartyServer_Tests import *
from Business_Gateway.RecruitServer_Tests import *
from MicroService.OrderServer_Tests import *
from MicroService.SelfProductServer_Tests import *
from MicroService.ReceiptServer_Tests import *
from MicroService.ProductServer_Tests import *
from MicroService.MediaServer_Tests import *
from MicroService.BankRollServer_Tests import *
from MicroService.ArbiterServer_Tests import *




cacheEnable = os.getenv("CacheEnable",'True')

def testlist(port):
    common = Common()
    common.cache(cacheEnable)#缓存
    testlist = list()
    testlist.clear()
    if port == str(servers.Homepage.value):
        homepage = Run_HomePage_Test
        return {homepage.home_page}
    elif port == str(servers.Door.value):
        pass
    elif port == str(servers.Main.value):
        pass

# 业务网关
    elif port == str(servers.Teacher.value):
        # common.insert_mservice_data(servers.Teacher.name)  # 微网关数据,测试前先灌数据
        # co= common.waitformservice(timeout=600,interval=5,server=servers.Teacher.name)
        # if co:
            teacher = Run_Teacherserver_Test
            testlist.append(teacher.teacheractivities_query_获取我发布的广告)
            testlist.append(teacher.teacherexpertpromotions_query_查询全部高知专家推广)
            return testlist

    elif port == str(servers.Book.value):
        book = Run_bookserver_Test
        testlist.append(book.bookinformations_search_搜索书_本市)
        testlist.append(book.bookinformations_search_搜索书_周边)
        testlist.append(book.bookinformations_search_搜索书_外市)
        testlist.append(book.bookinfomation_myself_获取我的书信息)
        testlist.append(book.bookinfomation_query_owners_获取我有意的书和人)
        testlist.append(book.bookinfomation_query_fans_获取对我的书有兴趣的人与书)
        testlist.append(book.bookinfomation_pushbooks_获取朋友推荐的书)
        testlist.append(book.bookactivities_query_getjoin_获取活动报名的人)
        testlist.append(book.bookactivities_query_getconsult_获取活动咨询的人)
        testlist.append(book.bookactivities_myself_query_获取我报名咨询的活动)
        testlist.append(book.bookactivities_query_getcollection_获取我收藏的活动)
        testlist.append(book.bookactivities_query_advert_获取一组轮播广告)
        return testlist

    elif port == str(servers.SchoolMate.value):
        schoolmate = Run_SchoolMateserver_Test
        testlist.append(schoolmate.campusrecruitment_query_recent_查询近期的单位校招)
        testlist.append(schoolmate.campusrecruitment_query_resume_查询校招被投递的简历)
        return testlist

    elif port == str(servers.MindStreet.value):
        mindstreet = Run_MindStreetserver_Test
        testlist.append(mindstreet.mindstreets_others_获取普通类别的列表)
        testlist.append(mindstreet.mindstreets_secondhands_获取二手类别的列表)
        testlist.append(mindstreet.mindstreets_intention_获取意向客户)
        testlist.append(mindstreet.mindstreets_allcustomers_获取店铺总客户量)
        testlist.append(mindstreet.collegestreets_publish_college_获取筛选大学)
        testlist.append(mindstreet.collegestreets_collegestreets_获取校区街商品类别列表)
        testlist.append(mindstreet.collegestreets_collection_hand_获取我校区街商品类收藏列表)
        testlist.append(mindstreet.mindstreets_community_获取发布周边的社区)
        testlist.append(mindstreet.mindstreets_stroll_community_获取逛周边的社区)
        testlist.append(mindstreet.mindstreets_markets_获取超市类别列表)
        testlist.append(mindstreet.myreserves_myself_获取我的预定)
        testlist.append(mindstreet.myreserves_nowpeople_获取本期该商品预定的人)
        testlist.append(mindstreet.streetevaluations_check_查看评价)
        return testlist

    elif port == str(servers.RentHouse.value):
        renthouse = Run_RentHouseserver_Test
        testlist.append(renthouse.housingresourceenums_query_districtarea_查询所有片区)
        testlist.append(renthouse.housingresourceenums_query_metroline_查询所有地铁站点)
        testlist.append(renthouse.housingresoureceenums_创建一个房源)
        return testlist

    elif port == str(servers.Lease.value):
        lease = Run_Leaseserver_Test
        testlist.append(lease.forleases_query_搜索租赁)
        testlist.append(lease.rents_query_按条件搜索出租)
        return testlist

    elif port == str(servers.Job.value):
        job = Run_Jobserver_Test
        testlist.append(job.positions_query_批量查询职位)
        testlist.append(job.positions_buildadvert_查询招聘职位广告_本楼职业交流群)
        testlist.append(job.positions_jobadvert_查询招聘广告_本楼职位招牌群)
        testlist.append(job.resumes_query_批量查询简历)
        testlist.append(job.jobcomments_query_查询点评)
        return testlist

    elif port == str(servers.Club.value):
        club = Run_Clubserver_Test
        testlist.append(club.ceoagrees_query_mylover_查询我赞同的人)
        testlist.append(club.ceoagrees_query_loveme_查询投票给我的人)
        testlist.append(club.ceoclubapplys_query_分页获取等待投票的人)
        testlist.append(club.ceomythinktasks_query_mylover_查询我的智库)
        testlist.append(club.ceomythinktasks_query_loveme_查询我是谁的智库)
        testlist.append(club.ceomythinktasks_filter_获取可添加的智库)
        testlist.append(club.lovemyloves_query_mylover_查询我的意中人)
        return testlist

    elif port == str(servers.Figure.value):
        figure = Run_Figureserver_Test
        testlist.append(figure.ceobuildingscaneds_ceoreport_ceo显示楼层信息)
        testlist.append(figure.contactpersonrecords_query_job_获取我想交往的人列表_职场人物)
        testlist.append(figure.contactpersonrecords_query_interest_获取我想交往的人列表_兴趣)
        testlist.append(figure.lovefigureactivities_query_获取我发布的广告)
        testlist.append(figure.lovefigureparticipators_query_获取该广告的参与者)
        testlist.append(figure.lovefigureparticipators_query_collection_获取收藏或报名的活动)
        testlist.append(figure.microposts_查看帖子列表)
        testlist.append(figure.microposts_topicid_replies_对帖子获取评论列表)
        return testlist

    elif port == str(servers.LifeSupply.value):
        lifesupply = Run_LifeSupplyserver_Test
        testlist.append(lifesupply.lifesupplygoodses_myself_goods_获取我的货源)
        testlist.append(lifesupply.lifesupplygoodses_seller_goods_卖家获取货源)
        testlist.append(lifesupply.lifesupplygoodses_find_goods_卖家查找货源)
        testlist.append(lifesupply.lifesupplygoodses_collection_获取我的收藏)
        testlist.append(lifesupply.lifesupplygoodses_evaluation_查看评价)
        testlist.append(lifesupply.lifesupplygoodses_intention_获取意向客户)
        testlist.append(lifesupply.lifesupplygoodses_chance_查看剩余次数)
        return testlist

    elif port == str(servers.Interest.value):
        interest = Run_Interestserver_Test
        testlist.append(interest.aroundpersons_获取我周围的人)
        return testlist

    elif port == str(servers.Gift.value):
        gift = Run_Giftserver_Test
        testlist.append(gift.giftcomments_获取礼物赠言集合)
        testlist.append(gift.gift_todayreceive_今日收到)
        testlist.append(gift.gift_receivegifts_获取收到的礼物集合)
        testlist.append(gift.gift_receivedetails_获取收到的礼物集合明细)
        testlist.append(gift.gift_sentgifts_获取送出的礼物集合)
        return testlist

    elif port == str(servers.Conference.value):
        conference = Run_Conferenceserver_Test
        testlist.append(conference.ceoconferencejoins_query_会议所有报名人)
        testlist.append(conference.ceoconferencejoins_attentionandjoin_查询我的关注和参会)
        testlist.append(conference.datingagencys_query_获取相亲承办机构)
        testlist.append(conference.loveconferences_query_查询相亲聚会)
        return testlist

    elif port == str(servers.Party.value):
        party = Run_Partyserver_Test
        testlist.append(party.ceopartyjoins_joinparties_邀请我的聚会)
        testlist.append(party.ceopartyjoins_inviteparties_特邀我的聚会)
        testlist.append(party.ceopartys_advert_查询私人小聚广告)
        return  testlist

    elif port == str(servers.Recruit.value):
        recruit = Run_Recruitserver_Test
        return testlist


#微服务
    elif port == str(servers.Order.value):
        order = Run_Orderserver_Test
        testlist.append(order.orderreports_water_total_获取接单总计)
        testlist.append(order.orderreports_water_totaldetail_获取接单总计明细)
        testlist.append(order.orders_some_获取批量订单用于支付)
        testlist.append(order.orders_query_查询订单)
        testlist.append(order.orders_toreciptorder_查询可开发票订单)
        testlist.append(order.orders_undelivery_查询未发货订单_商品产品)
        testlist.append(order.orders_delivery_查询已发货订单_商品产品)
        testlist.append(order.orders_water_group_查询订单分组_接单)
        testlist.append(order.orders_water_grouporder_查询订单分组_接单)
        testlist.append(order.orders_water_myorder_查询我的定水订单)
        return testlist

    elif port == str(servers.User.value):
        user = Run_Userserver_Test
        testlist.append(user.faces_userlogotags_批量获取用户的头像标签)
        testlist.append(user.faces_userlogotags_byscenes_根据场景一一对应批量获取用户的头像标签)
        testlist.append(user.faces_userlogotags_withdirection_批量获取用户的头像标签及相对位置)
        testlist.append(user.souls_list_根据id列表批量获取实体)
        testlist.append(user.piles_list_根据id列表批量获取大楼)
        testlist.append(user.deliveryaddresses_query_查询)
        testlist.append(user.pile_id_directions_相对指定大楼返回一批用户的相对位置)
        testlist.append(user.piles_query_bykey_根据关键字返回一批已注册pile及被选未注册数据)
        testlist.append(user.user_list_work_获取work用户列表)
        return testlist

    elif port == str(servers.Param.value):
        param = Run_Paramserver_Test
        testlist.append(param.userservices_list_根据列表批量获取实体)
        testlist.append(param.usertariffs_list_系统产品)
        testlist.append(param.usertariffs_timeadvert_list_时间广告)
        testlist.append(param.usertariffs_conference_list_重要会议)
        testlist.append(param.usertariffs_supplier_list_社区供应商)
        return testlist

    elif port == str(servers.Tip.value):
        tip = Run_Tipserver_Test
        testlist.append(tip.awards_query_搜索)
        testlist.append(tip.awards_query_total_搜索合计)
        return testlist

    elif port == str(servers.SelfProduct.value):
        selfproduct = Run_SelfProductserver_Test
        testlist.append(selfproduct.hawings_list_创建卖家多个摆摊)
        testlist.append(selfproduct.hawings_bysellers_用户搜索卖家们可供商品每卖家每种商品只会有一个统一分组价格会自我调节)
        testlist.append(selfproduct.hawkings_sellerhawkings_根据卖家ids和产品ids获取摆摊)
        testlist.append(selfproduct.selfproducts_query_搜索)
        return testlist

    elif port == str(servers.Receipt.value):
        receipt = Run_Receiptserver_Test
        testlist.append(receipt.newreceipt_query_all_卖家查询发票)
        testlist.append(receipt.newreceipt_query_need_卖家获取需要开票信息)
        testlist.append(receipt.newreceipt_query_need_detail_卖家获取用户需要开票信息)
        return testlist

    elif port == str(servers.Product.value):
        product = Run_Productserver_Test
        testlist.append(product.product_query_查询产品)
        testlist.append(product.product_query_nearby_查询附近产品)
        return testlist

    elif port == str(servers.Media.value):
        media = Run_Mediaserver_Test
        testlist.append(media.photos_schoolmatephoto_获取图片分页集合)
        testlist.append(media.photos_hometownphoto_获取图片分页集合)
        return testlist

    elif port == str(servers.BankRoll.value):
        bankroll = Run_Bankrollserver_Test
        testlist.append(bankroll.sellers_sellerid_transflows_list_根据id列表获取实体)
        testlist.append(bankroll.sellers_sellerid_transflows_query_查询卖家交易流水)
        testlist.append(bankroll.users_transflows_query_查询用户交易流水)
        testlist.append(bankroll.users_transflows_获取分页用户资金流水信息)
        return testlist

    elif port == str(servers.Arbiter.value):
        arbiter = Run_Arbiterserver_Test
        testlist.append(arbiter.appeals_query_搜索)
        testlist.append(arbiter.applys_query_搜索)
        return testlist




