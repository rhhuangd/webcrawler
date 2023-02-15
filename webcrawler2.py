import urllib.request as req
import bs4

# 從網站最新頁抓取資料, 傳回下一頁網址
def GetData(url):
    # 抓取 ptt 八卦版資料需要多附加 Cookie: over18=1
    request = req.Request(url, headers={
        "Cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    })

    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
            titleGossiping.write(title.a.string + "\n")
        else:
            print(title.string.strip())
            titleGossiping.write(title.string.strip() + "\n")
    
    nextURL = root.find("a", string="‹ 上頁")
    return nextURL["href"]

# 一次抓取多頁內容: 從當前網站抓取資料, 得到下一頁網址後傳回並重複抓取動作
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
titleGossiping = open("titleGossiping.text", mode="w", encoding="utf-8")
count = 0
while count < 5:
    url = "https://www.ptt.cc" + GetData(url) 
    count += 1
titleGossiping.close()