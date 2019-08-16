letters=["a","b","c","d","e"]

print(letters)
#print(letters[0])  #印出letters串列中索引值0的位置
#print(letters[-1])
#print(letters[0:-1])

"""串列的新增"""
   #letters.append("f")   # 新增一個"f"元素到letters串列尾端
   #letters.insert(0,"g") # 將"g"元素插入letters串列中的第一個位置

"""串列的修改"""
   #letters[1]="h"# 將letters串列中的第2個元素值更改成"h"

"""串列的刪除"""
'''1  del'''
  # del letters[1]         # 刪除letters串列中的第二個元素

'''2  pop()'''
    #1  letters.pop() # 從letters串列尾端彈出一個項目

    #2  value=letters.pop(1) # 將letters串列尾端彈出的一個項目存到value變數中
    #2  print(value) # 印出value值
   
'''3 remove()'''
    #1  letters.remove("c") # 刪除letters串列中的"c"元素

   
    #2  value="c"
    #2  letters.remove(value) # 刪除etters串列中的"c"元素
  
print(letters)
print(min(letters))


letters2=["C","E","D","B","A"]

"""串列的排序"""
'''sort()...永久'''
  # letters2.sort()# 將letters2串列依字母順序進行排列
  # letters2.sort(reverse=True) # 將letters2串列進行反序排列
'''sorted()...暫時  '''   
  # L2_sorted =  sorted(letters2)   # 印出暫時依字母順序排列的letters2串列
  # L2_sorted = sorted(letters2,reverse=True)   # 印出暫時依字母反序排列的letters2串列 
  # print(L2_sorted)
'''reverse()...反向'''
  #letters2.reverse() # 把letters2串列的順序反轉


print(letters2)


