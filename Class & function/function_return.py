#return_Argument(引數) 
def get_location(city,area,zipcode): # 定義一個get_location函式需要三個引數
    location=city+" "+area+" "+zipcode
    return location # 返回location

return_value=get_location("台南市","永康區","145") # 把返回值指定存放在return_value變數中
print(return_value)


#return_dictionary
def get_name(first_name,last_name): # get_name函式接收first_name和last_name
    name={"first":first_name,"last":last_name} # 將收到的first_name值對應到first鍵，將last_name值存到last鍵，再將兩的鍵值對存到name字典
    return name # 返回name字典

return_value=get_name("gong","jia-qing")
print(return_value)

#return_array
def get_name(names):
    for name in names:
        print("hello,"+name)
        
usernames=["bonny","steven","jack","rose"]
get_name(usernames) # 將usernames串列傳入get_name函式中




#v#return_while
def get_name(first_name,last_name):
    name=first_name+" "+last_name
    return name

while True:
    print("enter 'q' at any time to quit") # 新增一條文字告知使用者如何隨時跳出迴圈
    
    first=input("enter your first name :")
    if first =="q": # 當使用者輸入"q"則跳出迴圈
        break
    last=input("enter your last name :")
    if last =="q": # 當使用者輸入"q"則跳出迴圈
        break
        
    print(get_name(first,last)) # 呼叫get_name函式接收輸入的first值和last值

















