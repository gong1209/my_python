name = input("please enter your name : ")
print("hello,"+name) # 因為name是字串所以可以直接跟"hello,"字串相加

age = input("how old are you ?") # 使用者輸入的東西都算是字串
age = int(age) # 將age變數轉成int的型態再傳回age變數中
if age >= 20 : # age變數轉為數值後才可以比大小不然會出錯
    print("can vote")
else :
    print("can't vote")


text = "aaAaAaAaAaaaaAaAaaaAaAaAAAaaaaAaaAa" 
find = input("which word do you want to find (A or a) ? ") # 輸入一個值存到find變數中

print(text.count(find)) # 用count()方法來找find變數的值在text字串裡出現幾次

