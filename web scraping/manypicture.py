import requests
from bs4 import BeautifulSoup
import shutil

res = requests.get("http://www.gamebase.com.tw/forum/64172/topic/96278769/1")
#print(res.text)
soup = BeautifulSoup(res.text)
for img in soup.select(".img") :
    #print(img["src"])
    fname = img["src"].split('/')[-1]  # 取檔名

    #print(picname)

    ##存圖片
    path ="C:\\Users\\user\\Desktop\\VScode\\python\\web scraping\\pic\\"

    res2 = requests.get(img["src"],stream=True)
    f=open(path+fname,"wb")
    shutil.copyfileobj(res2.raw,f)

    f.close()
    print(path + fname)
    del res2
















