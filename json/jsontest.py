import json 

with open("jsontest.txt")  as jtot :
    d=jtot.read()
    print(d)
    print(type(d))


with open("testjson.json",'w')  as ttoj :
    json.dump(d,ttoj)
    

with open("testjson.json") as file: 
    k=json.load(file)
    print(k)   
    print(type(k))



    