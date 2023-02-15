# 裝飾器 decorator
# 先執行裝飾器內部函式, 再執行呼叫的函式
# def decorator1(callbackfunc):
#     def preFunc():
#         print("Run decorator1")
#         callbackfunc()
#     return preFunc

# @decorator1
# def testFunc():
#     print("Run actual function")

# testFunc()

# 裝飾器工廠 decorator factory (可以丟參數)
# def decoFactory(firstName, lastName):
#     def decorator2(callbackfunc):
#         def preFunc():
#             fullName = firstName + " " + lastName
#             callbackfunc(fullName)
#         return preFunc
#     return decorator2

# @decoFactory("Ryan", "Huang")
# def sampleFunc(decoResult):
#     print(decoResult)

# sampleFunc()


#裝飾器可重複利用 (錯誤版: callbackfunc放錯位置, 也可執行why?)
# from datetime import datetime
# def decoratorNowTimeCreate():
#     def preRun(callbackfunc):
#         timeNow = datetime.now()
#         callbackfunc(timeNow)
#     return preRun

# @decoratorNowTimeCreate()
# def showYear(time):
#     print(time.year)

# @decoratorNowTimeCreate()
# def showDay(time):
#     print(time.day)   

# showYear
# showDay

# 正確版: 附加裝飾器不用加()
from datetime import datetime
def decoratorNowTimeCreate(callbackfunc):
    def preRun():
        timeNow = datetime.now()
        callbackfunc(timeNow)
    return preRun

@decoratorNowTimeCreate
def showDate(time):
    print(time.date())

@decoratorNowTimeCreate
def showTime(time):
    print(time.time())   

showDate()
showTime()