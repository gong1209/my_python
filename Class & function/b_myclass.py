class Human:
    def __init__(self,h=0,w=0):
        self.height=h
        self.weight=w
    def BMI(self):
        return self.weight / ((self.height/100)**2)

    def __gt__(self,other):  ## other - 比較
        return float(self.BMI()) > float(other.BMI())

        '''__lt__ 小於(<)
           __le__ 小於等於(<=)
           __eq__ 等於(==)
           __ne__ 不等於(!=)
           __gt__ 大於(>)
           __ge__ 大於等於(>=)'''

    def __add__(self,other):    # other - 運算
        return self.height + other.height
    def __iadd__(self,other):
        self.height += other.height
        self.weight += other.weight
        return self

        # __add__  +           __iadd__  +=
        # __sub__  -           __isub__  -=
        # __mul__  *           __imul__  *=
        # __truediv__   /      __itruediv__   /=
        # __floordiv__  //     __ifloordiv__  //=
        # __mod__  %           __imod__  %=
        # __pow__  **          __ipow__  **=



'''私有屬性、私有方法'''
class Human_p:
    def __init__(self,hp=0,wp=0):
        self.__height_p=hp
        self.__weight_p=wp

    def __BMI(self):
        return self.__weight_p / ((self.__height_p /100)**2)

    def getBMI(self):       #間接存取私有方法
        return self.__BMI()



    






