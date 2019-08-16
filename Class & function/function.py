def hello_world(): 
    print("hello world")

hello_world() # 呼叫hello_world()函式


def greet(name): 
    print("hello,"+name)
    
greet("Gong") # 呼叫greet()函式


#位置引數
def pets(pet_name,pet_type): # 定義pets函式需要兩個引數
    print("I have a "+pet_type+" and its name is "+pet_name)

pets("dog","tony") # 我有一隻tony 叫做 dog  
pets("cat","candy")


#關鍵字引數
pets(pet_type="dog",pet_name="tony") # 明確的指出pet_type對應dog、pet_name對應tony 
pets(pet_name="candy",pet_type="cat") 



#參數預設
def pet_cat(pet_name,pet_type="cat"): 
    print("I have a "+pet_type+" and its name is "+pet_name)

pet_cat(pet_name="tony") # 預設pet_type是dog所以只要傳入pet_name就好
pet_cat(pet_name="candy",pet_type="pig") # 如果不是dog的話就傳入新的pet_type它就不會使用預設值












