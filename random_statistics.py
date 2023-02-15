# 隨機亂數 random
import random

randomData = [1,2,3,4,55,66,77,88]
# print(random.choice(randomData))
# print(random.sample(randomData,5)) # 輸出為列表, 取樣數量大於資料列表數量會出錯 ValueError: Sample larger than population or is negative
# random.shuffle(randomData) # 隨機調換順序(洗牌)
# print(randomData) 
# print(random.random())
# print(random.uniform(0, 1000))
# print(random.normalvariate(100, 15))

# 統計模組 statistics
import statistics
print(statistics.mean(randomData))
print(statistics.median(randomData))
print(statistics.stdev(randomData))