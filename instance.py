from datetime import datetime
import math
from time import sleep
from typing import NewType

# 定義 停車格 類別
class ParkingSpace:

    def __init__(self):
        self.type = ""
        self.state = False
        self.enterTime = None
        self.checkTime = None 
        self.duration = None
        self.charged = False
        self.totalAmount = 0

    def Enter(self, type):
        self.type = type
        self.enterTime = datetime.now()
        print("停車時間" + str(self.enterTime))
    
    def ChargeAmount(self, type):
        if type == "vehicle":
            self.checkTime = datetime.now()
            self.duration = self.checkTime - self.enterTime
            if self.duration.seconds > 0: # Rule1: 半小時內免費, 超過半小時每半小時15元; Rule2: 一進場就開始計費, 每半小時15元
                self.totalAmount = (math.ceil(self.duration.seconds/60))*15 
        print("需繳費金額: " + str(self.totalAmount) + " 元")

    def Charged(self):
        self.charged = True
        print("已繳費")

    # 繳費後15分鐘內離場 檢查

    def Exit(self):  # 離場後重置屬性值
        self.type = ""
        self.state = False
        self.enterTime = None
        self.checkTime = None
        self.duration = None
        self.charged = False
        self.totalAmount = 0
        print("離開停車格")

newCar = ParkingSpace()
newCar.Enter("vehicle")
sleep(5)
newCar.ChargeAmount("vehicle")
sleep(5)
newCar.Charged()
sleep(5)
newCar.Exit()

