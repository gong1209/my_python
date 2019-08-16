#多元組 : 不可變的串列


numbers=(1,2,3) # 定義一個多元組
print("Original :") 
for number in numbers : # 在numbers多元組中取得元素再存到number變數中
    print(number) # 印出變數存到的值

numbers=(4,5,6,7) # 讓原本多元組(1,2,3)的值改為(4,5,6)
print("Modified :")
for number in numbers :
    print(number) 

location = ("tainan","stust",("123","ABC","abc"))
print(location)
print(location[2][1])
print(location[2][1][1])



a=3
b=4
a,b=b,a # 或寫成(a,b)=(b,a)
print(a)
print(b)












