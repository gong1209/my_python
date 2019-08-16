students={"a":"A+","b":"B+","c":"C+"}

NO_1=students["a"]
print(" The Highest score is " + NO_1)


"""新增鍵值對"""
#students["d"]="D+"

"""修改鍵值對"""
#students["a"]="E+"

"""刪除鍵值對"""
del students["b"]


print(students)

##建立dict的方法
dict_1 = dict({"a":1111,"b":2222,"c":3333})
#dict_2 = dict(a=1111,b=2222,c=3333)
#dict_3 = {"a":1111,"b":2222,"c":3333}


for v in dict_1.values():  ##值
    print(v)

for k in dict_1:        ##鍵
    print(k)
for k in dict_1.keys():
    print(k)






