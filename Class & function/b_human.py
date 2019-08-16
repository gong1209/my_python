import b_myclass

"""比較"""
a = b_myclass.Human(180,80)  ### a  BMI
print("a.BMI()",a.BMI())
b = b_myclass.Human(170,70)  ### b  BMI
print("b.BMI()",b.BMI())

print(a>b)  #T
print(b>a)  #F


"""運算"""
a = b_myclass.Human(180,80)
b = b_myclass.Human(170,70)
print(a+b)                 # 180+170    
print(a.height,a.weight)   # 180 80
a+=b                       #__iadd__
print(a.height,a.weight)   #350 150


'''私有屬性、私有方法'''
a = b_myclass.Human_p(180,80)

##(無法存取)
print(a.__height_p,a.__weight_p)  #AttributeError: 'Human' object has no attribute '__height'
print(a.BMI())     #AttributeError: 'Human' object has no attribute 'BMI'

##(間接存取)
print(a.getBMI())


