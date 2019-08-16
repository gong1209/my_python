# 匯入單個類別
from C_car import Car # import陳述句會讓python開啟car模組並匯入Car類別

car1 = Car(2018,"toyota","black") 
car1.get_name() 

print("\n")

#匯入多個類別
from C_car import Car,ElectricCar # import陳述句會讓python開啟car模組並匯入Car和Electric類別

car1 = Car(2019,"toyota","black") 
car1.get_name()
car1.update_mile(87)
car1.get_mile()

ecar1 = ElectricCar(2019,"benz","white")
ecar1.get_name()
ecar1.get_battery()

# 匯入整個模組
import C_car # import整個car模組

car1 = C_car.Car(2019,"toyota","black") # 建立一個car1實例並用<模組名稱.類別名稱>語法來存取需要的類別 
car1.get_name()

ecar1 = C_car.ElectricCar(2019,"benz","white")
ecar1.get_name()



















