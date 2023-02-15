import urllib.request as req

for pageIndex in range(3999, 3997, -1):
    url = "https://www.ptt.cc/bbs/Tech_Job/index" + str(pageIndex) + ".html"
    print("抓取網站位址:" + url)

    #建立一個附加Request Headers資訊的Request物件
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)

    #解析html原始碼, 擷取文章名稱
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    # print(root.title.string)
    # title = root.find("div", class_= "title") # 尋找 class=title 的 div 標籤 
    # print(title.a.string)
    articleTitle = open("articleTitle.txt", mode="a+", encoding="utf-8")
    titles = root.find_all("div", class_ = "title") # 尋找所有 class=title 的 div 標籤 
    for title in titles:
        if title.a != None: # 若標題包含 a 標籤 (未刪除的文章)
            print(title.a.string)
            articleTitle.write(title.a.string+"\n")
        else: # 沒有 a 標籤 (已刪除文章)
            print(title.string.strip())
            articleTitle.write(title.string.strip()+"\n")
    articleTitle.close()

    # 找當前頁面的上一頁
    # btns = root.find("div", class_="btn-group btn-group-paging") # 尋找 class=btn-group btn-group-paging 的 div 標籤
    # btn = root.find("a", string="‹ 上頁")
    # print(btn)
    # subURL = btn.get("href") # 獲得屬性值: get(屬性字串)
    # print(newURL)

# Note:      
# find_all() output 為列表
