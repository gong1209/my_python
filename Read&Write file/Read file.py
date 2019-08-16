#read-1
with open("Zen of Python.txt") as file_object: # 開啟number.txt檔並將其存到file_object中
    content=file_object.read() # 讀取file_object的所有內容
    print(content.rstrip()) # 將印出的檔案刪除read()返回的一行空白

''' read - 2
f = open('Zen of Python.txt','r')
print(f.read())
'''

#raed -line by line
with open("Zen of Python.txt") as file_object: 
    for line in file_object: 
        print(line)
        #print(line.rstrip()) #無空行




'''
w	讀取模式				
r   寫入模式
a   附加檔案
r+  可讀取寫入模式
'''