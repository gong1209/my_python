import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.books.com.tw/search/query/cat/all/key/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/v/1")
#print(res.text)

soup = BeautifulSoup(res.text) 

for item in soup.select(".item") : ## .item(商品) ， b(價錢)
    price=item.select("b")[0].text        ##取價錢(純數字)
    name = item.select("h3")[0].text   ##代表的是list中的第一筆，.text則可以取得不含 html 標籤的純文字內容。
    print(name,"---",price," dolls\n")
    



