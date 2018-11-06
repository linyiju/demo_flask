#時間套件
import time

# localdate = time.strftime("%Y-%m-%d")#日期
# localtime = time.strftime("%H:%M:%S")#時間 24小時至

# data = {"date":localdate, "time":localtime}


def get_date():
	localdate = time.strftime("%Y-%m-%d",time.localtime())
	return localdate

def get_time():
    localtime = time.strftime("%H:%M:%S",time.localtime())
    return localtime
# def time():
#     localtime = time.strftime("%H:%M:%S")#時間 24小時至
#     return localtime