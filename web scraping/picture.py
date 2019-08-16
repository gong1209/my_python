import requests
import shutil

url="https://www.largitdata.com/static/img/logo-footer.jpg"
res = requests.get(url,stream=True)  #steam=True 允許下載
print(res)

f = open ("image.png","wb") ##wb : 二進制寫入(圖片)
shutil.copyfileobj(res.raw,f)          #shutil.copyfileobj(fsrc, fdst[, length]) 
                                        #复制file-like对象fsrc的内容到fdst，如果fdst不存在则自动创建。
f.close()                              #length表示缓冲大小，如果是负数表示直接复制，不循环遍历块中的源数据。

#print(res.raw)                      # 数据默认按块读取(16 * 1024)避免不可控的内存消耗。





