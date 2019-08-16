colors=["red","orange","yellow","green","blue"]
print(colors[0:3]) # 印出索引足標0,1,2對應的元素   012
print(colors[1:4]) # 印出索引足標1,2,3對應的元素   123
print(colors[:2]) # 印出從索引足標0到1的元素   01
print(colors[2:]) # 印出從索引足標2到最後的元素   234
print(colors[-2:]) # 印出從索引足標-2(也就是倒數第二個)到最後的元素  34

print("\n")
    
for color in  colors[0:3] :
    print(color)

print("\n")

my_pets=["dog","cat","bird"] # 建立一個my_pets串列
friend_pets=my_pets[:] # 將my_pets串列複製到friend_pets串列

my_pets.append("rabbit") # 新增一個元素到my_pets串列
friend_pets.append("turtle") # 新增一個元素到friend_pets串列
print("My pets :")
print(my_pets) # 印出my_pets串列
print("Friend's pets :")
print(friend_pets) # 印出friend_pets串列










