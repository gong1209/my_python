num = input("please enter a number : ")
num = int(num) # 將number變數轉成int的型態再傳回number變數中




if num>1 :
  for i in range(2,num):

    if (num % i)==0 :
      print(num, " is not Prime number")
      print(i," X ",num//i," = ",num)
      break
  else :   
     print(num , " is  Prime number")    
else:
   print(num," is not Prime number")






