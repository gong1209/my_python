import random                     
  
"""little bug : 數字可重複，AB數字有誤 """
A=0                                     ##guess number game   
B=0                                        

n=random.randint(0,9999)
if len(str(n))==4:   
    n=str(n) 
elif len(str(n))==3:   
    n="0"+str(n)  
elif len(str(n))==2:   
    n="00"+str(n)
elif len(str(n))==1:   
    n="000"+str(n) 
print(n)


guess=[]
while True :
    ans=input("your answer is ? ")

    if len(ans)!=4  :
        print("Please enter four number !")
        guess.append("error")
        print(guess)
        continue

    guess.append(ans)

    print(guess)
    
    for i in range(4) :   ##A
        if ans[i]==str(n)[i]:
            A+=1

    for j in range(4) :   ##B 
        if ans[i]==str(n)[j] and i!=j :
            B+=1
            B-=A
    if A==4 :
        print("You win the game !")
        print("You guess ",str(len(guess)),"times !")
        break
    print(n)       
    print("%d A %d B" %(A,B) )
    A=0
    B=0

            









#count()




