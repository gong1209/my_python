str1 = 'hello python'
str2 = str1
# str2[0] = 'y'
# a = a + b could be written as a += b
str2 += ' journey'
print(str2 is str1)  #是否相同?

print(str1)
result = str2.split(' ') #字串以' '隔開成陣列
print(result)
result_back = '***'.join(result)  #字串用'***'組合
print(result_back)




