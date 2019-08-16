file=open("test.txt")

a=[]
while True :
    f=file.readline()
    if f=='' :
        break
    a.append(f)


print(a)



file=open("test.txt")  

for line in file.readlines():                           
    line = line.strip()                            
    print(line) 
file.close()