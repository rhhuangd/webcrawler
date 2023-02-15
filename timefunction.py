import time
from datetime import datetime, timedelta

# 計算兩個時間差
# 給定兩個固定時間_1: striptime()
datetime1 = datetime.strptime("201111", "%H%M%S")  # string -> datetime
datetime2 = datetime.strptime("220510", "%H%M%S")
duration = datetime2 - datetime1 # datatype: timedelta
print(duration.seconds/60) # 換算成分鐘

# 給定兩個固定時間_2: timedelta()
# datetime1 = timedelta(hours=20, minutes=30, seconds=30)
# datetime2 = timedelta(hours=21, minutes=25, seconds=35)
# duration = datetime2 - datetime1 # datatype: timedelta
# print(duration) 

# 取得相對值: sleep()
# timeNow = time.time() # datatype: float
# print(timeNow) # output: 從1970年開始至今的時間(以秒來表示)
# time.sleep(5)
# duration = time.time() - timeNow # datatype: float
# print(duration)