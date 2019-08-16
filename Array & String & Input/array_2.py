
list=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2]

#1
num=1
if num in list : 
    print(str(num)+" in list"  )
elif num not in list :
    print(str(num)+" not in list" )


#2
print("len: "+str(len(list)))

print("max: "+str(max(list)))
print("min: "+str(min(list)))
print("count: "+str(list.count(num)))


#3
i=0
j=5
try :
    list.index(num,i,j)
except :
    pass
else :
    print(str(num)+" in "+str(i)+"~"+str(j))



letters=["a","b","c","d","e"]

# letters[0]="f"
# letters[0:3]="f"  # "a","b","c"  ==> "f"
#(?) letters[0:3:2]="f"  # index從i到j的元素，以step為k的方式，將內容置換為X

# del letters[0:3]   #index從i到j的元素刪除
#(?) del letters[0:3:2]   #index從i到j的元素，以step為k的方式刪除元素


# letters.append("f")
# letters.clear()
# letters.copy()  #  = letters[:]
# letters.extend("f")  #  ==> letters=letters +"f"
# letters.insert(0,"f")
# letters.pop([0])
# letters.remove("a")
# letters.reverse()


print(letters)















