
#匿名函式

a = lambda x: x*x
print(a(3))
a = lambda x: x*x*x
print(a(3))
a = lambda s: "hello "+s
print(a("syu"))


a = lambda x,y,z: (x+y+z)/2
print(a(3,7,5))
a = lambda s,u,d: "hello "+s+",ans="+str(u+d)
print(a("syu",7,3))