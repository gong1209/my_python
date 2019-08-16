"""function & Argument(引數) 應用"""

#一個星號(建立空多元組tuple)
def get_name(*names): # *names參數中的星號會讓python建立一個名字為names的空多元組
    for name in names:
        print("hello,"+name)
        print(names)
    
get_name("bonny","steven")
get_name("jack")
get_name("rose","john","jane")

'''what use for-loop?    A:多元組不能跟字串相加'''


#兩個星號(建立空字典)
def users(first_name,last_name,**user_info): # **user_info參數中的星號會讓python建立一個名字為user_info的空字典
    user={}  
    user["first"]=first_name # 將first_name新增至user字典
    user["last"]=last_name # 將last_name新增至user字典
    for key,value in user_info.items(): # 用迴圈遍訪user_info裡的鍵值對並將其新增至user字典
        user[key]=value
    return user
    
user1=users("bonny","chang",city="taipei")
print(user1)
user2=users("steven","chang",city="taoyuan")
print(user2)
















