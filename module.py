import sys
print(sys.platform)
print(sys.maxsize)
sys.path.append("modules")
print(sys.path) # 印出模組的搜尋路徑
import modules.geometry as moduleGEO
result=moduleGEO.distance(1,1,5,5)
print(result)
slope=moduleGEO.slope(1,1,5,5)
print(slope)
