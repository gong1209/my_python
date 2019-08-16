number = input("please enter a number : ")
number = int(number) # 將number變數轉成int的型態再傳回number變數中


D0=int(number % 2 )
number /= 2
D1=int(number % 2 )
number /= 2
D2=int(number % 2 )
number /= 2
D3=int(number % 2 )
number /= 2

print(D3)
print(D2)
print(D1)
print(D0)






