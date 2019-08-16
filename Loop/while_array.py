number = 1
while number < 10 : # 當number<6的時候
    print(number) # 印出number
    number += 1 # number加一後再存回number中

print('\n')

#"""從某個串列般一項目到另一個串列"""

order=["hamburger","french fries","cola"]
already_cooked=[]

while order : # 如果order串列有東西while迴圈就會繼續執行
    cooking=order.pop() # 將order串列的值一一彈出來存到cooking變數中
    print("cooking :"+cooking)
    already_cooked.append(cooking) # 將cooking變數的值新增到already_cooked串列中

print(order)
print(already_cooked)

print("Finished :")
for cooked in already_cooked : # 告知python從already_cooked串列中取出值，並將取出的值存到cooked變數中

    print(cooked)



#""" 刪除串列中特定值 """

text = ["apple","apple","Finished","apple","apple", "while", "apple" , "apple","loop", "apple", "apple"]

while "apple" in text : # 當text串列中含有apple字串時，迴圈就會一直執行
    text.remove("apple") # 將text串列中的apple字串移除

print(text)












