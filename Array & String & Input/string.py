student_name="jia-qing gong"  #string
school="stust"  #string
student_id= 7   #int 
print(student_name.title())  #第一字大寫
print(student_name.upper())  #全大寫
print(student_name.lower())  #全小寫
print(len(student_name))
print(school+" "+student_name)
print(school+student_name)
print(school+" "+str(student_id)+" "+student_name)


print('This\'s python in VS code')   #內容含 ' 


##增加空白
print("hello\nworld")  # \n (換行) 
print("hello\n\tworld")  #\t (增加一個縮排)，預設縮排是四格?


#刪除空白
my_name=" gong"
print(my_name) #輸出結果為" gong"
print(my_name.lstrip()) #輸出結果為"gong"
print(my_name) #輸出結果為" gong"
print(" ") 

print(my_name) #輸出結果為" gong"
my_name = my_name.lstrip() #將去除左邊空白的字串存回變數中
print(my_name) #輸出結果為"gong"

 
"""統整
•	title()---讓第一個字大寫
•	upper()---讓全部變大寫
•	lower()---讓全部變小寫
•	len()---計算長度
•	\n---換行
•	\t ---空格
•	lstrip()刪除左邊空白、
•	rstrip()刪除右邊空白
•	strip()刪除兩邊空白
•	#---註釋
"""
#str cut
text = "0123456789"
print(text[-1:2:-2]) # 2(不含)~9(含) 以左二跳印
print(text[::2])
print(text[::-1])


## str.format() 應用  

##1
s = "The {0} {1} tower has {1} floors above ground and five underground.".format("taipei",101)
print(s) 
s = "The {} {} tower has {} floors above ground and five underground.".format("taipei",101,101)
print(s)
s = "The {location} {num} tower has {num} floors above ground and five underground.".format(num=101,location="taipei")
print(s)

##2    list
l = ["taipei","taichung","tainan",100,101,102]
s = "The {0[0]} {0[4]} tower has {0[4]} floors above ground and five underground.".format(l)
print(s)

##3 dictionary
d = {"city":"taipei","num":101}
s = "The {0[city]} {0[num]} tower has {0[num]} floors above ground and five underground.".format(d)
print(s)