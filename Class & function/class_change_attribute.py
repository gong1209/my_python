class Car():
    def __init__(self,year,brand,color):
        self.year = year
        self.brand = brand
        self.color = color
        self.miles = 0 # 建立一個miles屬性初始值為0
        
    def get_mile(self): # 定義一個get_mile方法可以存取miles
        print("Your " + self.brand+" has "+str(self.miles)+" miles on it")

    def get_color_year(self) :
     print("It's "+self.color +","+str(self.year) + " years old "  )


    # 新增一個update_mile方法來接收里程數值(就是mileage)，然後再存到self.miles裡        
    def update_mile(self,mileage): 
        self.miles = mileage

    def add_mile(self,kilometer): # 增加公里數
        self.miles += kilometer # 接收一個kilometer值加到self.miles裡
      
car1 = Car(10,"toyota","black") # 建立一個car1實例

car1.get_color_year()

'''#1 直接修改屬性Attribute的值'''
# car1.miles = 87 # 使用據點標示法來直接存取並設定出仔的miles屬性

'''#2 透過方法修改屬性Method的值'''
# car1.update_mile(87) # 呼叫update_mile方法並將87當作引數傳入mileage參數中

'''#3  利用方法進行值的增加'''
car1.update_mile(87)
car1.get_mile()
car1.add_mile(9400) # 呼叫add_mile方法並傳入9400



car1.get_mile() # 用實例呼叫get_mile方法








