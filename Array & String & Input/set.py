a={1,2,3,3,4,5,6}
print(type(a))
print(a)
b=frozenset({2,4,6})
print(type(b))
print(b)




a=set("tainan")    #等同於{"t","a","i","n","a","n"}
print(a)
b={"n","a","n"}    #等同於{"n","a","n"}
print(b)
print(a|b)  # |(聯集)
print(a&b)  # &(交集)
print(a-b)  # -(差集)
print(a^b)  # ^(對稱差集)
print(a<=b) # <=(是否為子集合)
print(a<b)  # <(是否為真子集)
print(a>=b) # >=(是否為母集合)
print(a>b)  # >(是否為真母集)



a={1,2,3,4}
print(a)
a.add(7)
print(a)
b = a.copy()  #不可寫成b=a , python 會將b參照到同一個物件,而不是複製一份
print(b)
b.clear()
print(b)
a.discard(1)
print(a)
a.remove(2)
print(a)
k=a.pop()
print(k)
print(a)