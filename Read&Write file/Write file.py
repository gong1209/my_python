filename="number.txt" 

'''
#寫入空檔案
with open(filename,"w") as file_object: # 以寫入模式開啟number.txt檔
    file_object.write("10 11 12") # 寫入第一行
    file_object.write("\n13 14 15") # 寫入第二行
'''

#附加到檔案後面
with open(filename,"a") as file_object: # 以附加模式開啟number.txt檔
   
    file_object.write("\n01234")
    file_object.write("\n56789")



f = open('tainan.txt','rb+')   #二進制開啟    
                                 
                              
f.seek(2)       #  f.seek(位移的bit數,0) - 從文件開頭開始
f.write(b'A')
#taApei city

f.seek(2,1)      #  f.seek(位移的bit數,1) - 從目前游標位置開始             
f.write(b'B')
#taApeB city

f.seek(-2,2)       #  f.seek(位移的bit數,2) - 從目前文件結尾開始
f.write(b'C')
#taApeB ciCy











