import random

min=1
max=99

ans=random.randint(min,max)

g=[]

while True:
    guess=input("please guess a number : ")
    g.append(guess)

    #檢查輸入的內容是否為數字
    try :
        guess=int(guess)
    except ValueError :
        print("please enter 'number'")
        continue

    #檢查輸入的數字是否介於規定範圍內
    if guess >max or guess < min :
        print("please enter number in  "+ str(min)+" ~ " + str(max))
        continue

    #判斷有沒有猜中密碼
    if ans==guess:
        print("B I N G O ! " +"answer is "+ str(ans) )
        print("You have guessed :" +str(len(g)) + " times ")
        break
    elif guess > ans :
        max = guess
        print("answer in "+ str(min)+" ~ " + str(max))
    elif guess < ans :
        min=guess
        print("answer in "+ str(min)+" ~ " + str(max))



