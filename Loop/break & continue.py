"""break範例"""
text = "enter your name or enter 'quit' to leave the program : "
while True : # 讓迴圈一直執行
    name = input(text) # 印出text字串將輸入的值存到name變數中
    
    if name == "quit" : # 當輸入quit時進入if區塊
        print("You\'ve left the program") 
        break  # 跳出迴圈

    else :
        print("NOt "+name +" ,please enter 'quit' " )  


"""continue的範例"""
number = 0
while number < 10 : # 當number<10就會繼續跑迴圈
    number += 1 
    if number % 2 != 0: # 判斷number是否不能被3整除
        continue # 如果不能被2整除就跳回迴圈一開始再加1
    
    print(number) # 如果可以被3整除就印出數字


"""無窮迴圈"""
x=1
while x< 3: # 當x<3
    print(x) # 印出x










