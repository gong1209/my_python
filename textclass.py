

"""簡易電話簿"""

mem={}

class member() :

    def  __init__(self,name,phone):
        self.name = name
        self.phone = phone
        #self.m="name: "+self.name +" , phone: "+self.name
        

    def add(self,name,phone) :

        while True :

            continue_prompt = input("Would you like to add someone ? (y/n)")
            if continue_prompt=="n": # 如果continue_prompt=="no"就跳出迴圈
                break
            elif continue_prompt=="y" :
                self.name=input("What's name you want to add?")
                self.phone=input("Your phone is ?")
                mem[self.name]=self.phone

        for i,j in mem.items() : 
            print("\tname: "+i +" \tphone: "+j)   
        #print(mem)

    def delete(self,name) :

        while True :

            continue_prompt = input("Would you like to delete someone ? (y/n)")
            if continue_prompt=="n": # 如果continue_prompt=="no"就跳出迴圈
                break
            elif continue_prompt=="y" :
                self.name=input("What's  name you want to delete?")
                if self.name not in mem :
                    print("can't find "+ self.name ) 
                    break
                else : 
                    del  mem[self.name]  

        for i,j in mem.items() : 
            print("\tname: "+i +" \tphone: "+j)      
        #print(mem)

    def list(self,name,phone) : 
        print("All member : ")
        for i,j in mem.items() : 
            print("\tname: "+i +" \tphone: "+j)   
        #print(mem)

    def correct(self,name) :
        while True :

            continue_prompt = input("Would you like to correct someone ? (y/n)")
            if continue_prompt=="n": # 如果continue_prompt=="no"就跳出迴圈
                break
            elif continue_prompt=="y" :
                new_name=input("What's  name you want to correct?")
                self.phone=input("Your new phone is ?")
                if new_name not in mem :
                    print("can't find "+ new_name ) 
                    break
                else : 
                    mem[new_name] =  self.phone

        for i,j in mem.items() : 
            print("\tname: "+i +" \tphone: "+j)      
        #print(mem)

        

name=input("What's your name?")
phone=input("Your phone is ?")

m=member(name,phone)

mem[name]=phone

while True :
    c= input("Would you like to do ? (1:add / 2:delete / 3:list / 4:correct / 5:end)")

    if c=="1": 
        m.add(name,phone)
    elif c=="2" :
        m.delete(str(name))
    elif c=="3" :
        m.list(name,phone)
    elif c=="4" :
        m.correct(str(name))
    elif c=="5" :
        break

with open("member.txt","w") as mb :
    mb.write("my Phone book\n")
    for i,j in mem.items() : 
        mb.write("name: "+i +" \tphone: "+j+"\n"  )




    
    




















