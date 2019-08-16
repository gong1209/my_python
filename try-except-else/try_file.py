filename="findword.txt"

try:
    with open(filename) as file:
        content=file.read()
except FileNotFoundError:  # 如果找不到檔案會執行這個區塊
    
    msg="Sorry,the file "+filename+" does not exist"
    print(msg)

    '''pass # 出錯時直接略過這個區塊'''
    
else: # 找到檔案會執行這個區塊
    find=input("find the word (a to e ) :")
    print(content.count(find))
finally : #一定執行
    print(str(find) + " was counted " +str(content.count(find)) +" times"   )
    




















