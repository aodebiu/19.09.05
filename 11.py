# # # import pytz
# # # # # from dateutil.parser import parse
# # # # # import datetime,time
# # # # # last_time = input("请输入：年，月，日，时，分，秒:")
# # # # # # last_time=datetime.datetime(2018,9,12,10,30,32,tzinfo=pytz.UTC)
# # # # # local_format = "%Y-%m-%d %H:%M:%S"
# # # # # time_str = last_time.strftime(local_format)
# # # # # last_time.strftime('%Y-%m-%d %H:%M:%S %Z')
# # # # # print(now_time)
# # # # # # now_time =
# # # #
# # # # # import datetime,time
# # # # # date_time=datetime.datetime(2018,9,12,10,30,32)
# # # # # return_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
# # # # # print(return_time)
# # # #
# # # # # def india_to_local(self,india_time_str,india_format = '%Y-%m-%dT%H:%M:%S+05:30'):
# # # # #     india_dt = datetime.datetime.strptime(india_time_str,india_format)
# # # # #     local_dt = india_dt + datetime.timedelta(hours=2, minutes=30)
# # # # #     # local_format = "%Y-%m-%d %H:%M:%S"
# # # # #     # time_str = local_dt.strftime(local_format)
# # # # #     # return time_str
# # # #
# # # # # import time
# # # # # import pytz
# # # # # import datetime
# # # # # date_=datetime.datetime(2018,6,19,20,55,00)
# # # # # timestamp2=date_.strftime('%Y-%m-%d %H:%M:%S') #date_.timetuple() 将datetime格式的转化为time模块的tuple格式
# # # # # print(timestamp2)
# # # # # def utc_to_local(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%SZ'):
# # # # #     local_tz = pytz.timezone('Asia/Chongqing')      #定义本地时区
# # # # #     local_format = "%Y-%m-%d %H:%M:%S"
# # # #
# # # # # def local_to_utc(local_ts, utc_format='%Y-%m-%dT%H:%MZ'):
# # # # #     local_tz = pytz.timezone('Asia/Shanghai')    #定义本地时区
# # # # #     local_format = "%Y-%m-%d %H:%M:%S"               #定义本地时间format
# # # # #
# # # # #     time_str = time.strftime(local_format, time.localtime(local_ts))    #首先将本地时间戳转化为时间元组，用strftime格式化成字符串
# # # # #     dt = datetime.datetime.strptime(time_str, local_format)             #将字符串用strptime 转为为datetime中 datetime格式
# # # # #     local_dt = local_tz.localize(dt, is_dst=None)                       #给时间添加时区，等价于 dt.replace(tzinfo=pytz.timezone('Asia/Chongqing'))
# # # # #     utc_dt = local_dt.astimezone(pytz.utc)                              #astimezone切换时区
# # # # #     return utc_dt.strftime(utc_format)                                  #返回世界时间格式
# # # # #
# # # # # # print(utc_to_local('2018-07-13T16:00:00Z', utc_format='%Y-%m-%dT%H:%M:%SZ'))
# # # # # print(local_to_utc(1531411200, utc_format='%Y-%m-%dT%H:%MZ'))
# # # #
# # # # from datetime import datetime, timedelta
# # # # import time
# # # # #
# # # # # # 字符串转datetime
# # # # # string = '2017-04-25 11:59:58'
# # # # # time1 = datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
# # # # # print(time1)
# # # # #
# # # # # # datetime转字符串
# # # # # time1_str = datetime.strftime(time1, '%Y-%m-%d %H:%M:%S')
# # # # # print(time1_str)
# # # # #
# # # # # # 时间戳转时间对象,这里用到的time模块是单独import time
# # # # # new_time = time.time()
# # # # # print(new_time)
# # # # # now_time = datetime.fromtimestamp(new_time)
# # # #
# # # # time_str = 'Wed May 09 00:00:00 CST 2018'
# # # # dt = datetime.datetime.strptime(time_str, "%a %b %d %X %Z %Y")
# #
# # import datetime,time
# #
# # from datetime import datetime
# # last_time=datetime.datetime(Wed,Dec,12,10,30,32,2018)
# # GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT+0800 (CST)'
# #
# # print(date.strftime(GMT_FORMAT))
# #
# # # dd = "Fri Nov 09 2018 14:41:35 GMT+0800 (CST)"
# # # GMT_FORMAT = '%a %b %d %Y %H:%M:%S GMT+0800 (CST)'
# # # print(datetime.strptime(dd, GMT_FORMAT))
# # # import datetime,time
# # # date_time=datetime.datetime(2018,9,12,10,30,32)
# # # return_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
# # # print(return_time)
#
# import datetime
# date_time = "Wed, Dec 12 10:30:32 2018 GMT+0500 (CST)"
# now_time1 = datetime.datetime.strptime(date_time, '%a, %b %d %H:%M:%S %Y GMT+0500 (CST)')
# now_time = datetime.datetime.strftime(now_time1,'%a, %b %d %Y %H:%M:%S GMT+0500 (CST)')
# now_time2 = datetime.datetime.strftime(now_time1,'%Y/%m/%d %H:%M:%S')
# print("变化前:"now_time)
# print("变化后:"now_time2)
#
# import datetime
#
# gmt = "Sun, 05 May 2019 00:00:00 GMT"
#
# # 第一步
# date1 = datetime.datetime.strptime(gmt, '%a, %d %b %Y %H:%M:%S GMT')
#
# print(date1)  # 输出: 2019-05-05 00:00:00
#
# # 第二步
# date2 = datetime.datetime.strftime(date1, '%Y-%m-%d')
#
# print(date2)  # 输出: 2019-05-05

import datetime,pytz
date_time = input("请按以下示例顺序输入Wed, Dec 12 10:30:32 2018：")
now_time = datetime.datetime.strptime(date_time, '%a, %b %d %H:%M:%S %Y')
now_time1 = datetime.datetime.strftime(now_time,'%a, %b %d %Y %H:%M:%S')
now_time2 = datetime.datetime.strftime(now_time,'%Y/%m/%d %H:%M:%S')
time_pytz1 = input("请输入之前时区名称例如Indian/Reunion:")
central = pytz.timezone(time_pytz1)
local_us = central.localize(now_time)
time_pytz2 = input("请输入需要转换地的时区格式同上:")
now_time2 = local_us.astimezone(pytz.timezone(time_pytz2))
print("变化前:",now_time1)
print("变化后:",now_time2)
pytz_info = pytz.common_timezones_set
print("时区选择：",pytz_info)
