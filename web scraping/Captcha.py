import requests
from bs4 import BeautifulSoup
from PIL import Image
import shutil

rs = requests.session() ##使用在多個觸發
##picture
pic_res = rs.get("https://www.boca.gov.tw/captcha.html",stream=True,verify=False)  #verify 设置为 False，Requests忽略对 SSL 证书的验证。
f=open("CaptchaCode.img","wb")
shutil.copyfileobj(pic_res.raw,f)
f.close()
img = Image.open("CaptchaCode.img")
img.show()

### post
url= "https://www.boca.gov.tw/sp-natr-queryresultm-1.html"
payload ={
'HIDIndex': '1',
'HIDQueryType': 'Single',
'LastName': '龔',
'FirstName': '家慶',
'CaptchaCode': ''
}

ver = input("Enter CaptchaCode :　")
payload['CaptchaCode']=ver

#print(payload)


res= rs.post(url,data=payload,verify=False)

res.encoding = "utf-8"
print(res.text)
soup=BeautifulSoup(res.text)
name = []
title=[]
all ={}
for item in soup.select(".aCenter") :
    print(item.text)
    name.append(item.text)
print(name)


for item2 in soup.select("th") : 
    print(item2.text)
    title.append(item2.text)
print(title)

'''i=0
j=0
for index in range(len(title)) :
    print(title[i],name[j])
    if i%6!=0 :
        i=0'''

