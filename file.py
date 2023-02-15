# 測試文檔讀寫
#########################################################################################
# testFile = open("testFile.txt", mode="w", encoding="utf-8") # utf-8編碼可寫入中文
# testFile.write("測試寫入功能20220120")
# testFile.close

# with open("testFile2.txt", mode="w", encoding="utf-8") as testFile2:
#     testFile2.write("操作文檔最佳實務方法\n") # write()會覆蓋舊有檔案內容, 若沒有該檔案會新建
#     testFile2.write("20220120")

# readFile = open("testFile2.txt", mode="r", encoding="utf-8") # 檔案有中文也要用utf-8編碼開啟, 不然會發生UnicodeDecodeError
# readContent = readFile.read()
# for line in readContent:
#     print(line)
# with open("testFile2.txt", mode="r", encoding="utf-8") as readContent:
#     for line in readContent:
#         print(line)
# readFile.close()
# print(readContent)

# 文檔用最佳實務方法與一般方法開啟後用for迴圈讀取內容得到的結果不同
###################################################################
# 最佳實務方法:
# 操作文檔最佳實務方法
#
# 20220120
#
# 一般方法:
# 操
# 作
# 文
# 檔
# 最
# 佳
# 實
# 務
# 方
# 法
# 
# 
# 2 
# 0 
# 2 
# 2 
# 0 
# 1 
# 2 
# 0 

#測試JSON格式檔案讀寫
############################################
import json
with open("config.json", mode="r") as jsonFile:
    jsonContent = json.load(jsonFile)  # 檔案類型為 字典
jsonContent["Birth"] = "1989/10/14" # 直接賦值新增
jsonContent.update({"Gender":"Male","Height":"176","Weight":"72"}) # 若要一次新增多組需使用update()
# 若已存在Key則覆蓋Value
with open("config.json", mode="w") as jsonFile2:
    json.dump(jsonContent, jsonFile2)
print(jsonContent)
# print("Name:", jsonContent["Name"])
# print("Age:", jsonContent["Age"])