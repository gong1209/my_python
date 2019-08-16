'''
▸ 以物件的概念來解決問題，稱為「物件導向程式設計」(Object-oriented programming, OOP)
▸ 支援物件的程式語言稱為「物件導向程式語言」(Object-oriented programming language, OOPL)，Python 屬此類語言
'''


class Dog(): # 建立一個Dog類別
    def __init__(self,name,age): 
        self.name=name # 取得name參數中的值並將其存入name變數中
        self.age=age # 取得age參數中的值並將其存入age變數中
    
    def eat(self): # 定義一個eat方法
        print(self.name + " is eating")
        
    def sleep(self): # 定義一個sleep方法
        print(self.name + " is sleeping")
        
dog1=Dog("tony",3) # 建立一個dog1實例
print("My dog's name is "+dog1.name+" and it's "+str(dog1.age)+" years old.")

dog1.eat() # 呼叫eat方法
dog1.sleep() # 呼叫sleep方法

dog2=Dog("candy",2)
print("Your dog's name is "+dog1.name+" and it's "+str(dog2.age)+" years old.")
dog1.eat() # 呼叫eat方法
dog2.sleep()























