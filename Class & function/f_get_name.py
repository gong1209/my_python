
import f_name
f_name.get_name("bonny")
f_name.get_name("jack","rose")

'''#使用as為模組指定別名
import f_name as fn
fn.get_name("bonny")
fn.get_name("jack","rose")'''


from f_name import get_name,get_city
get_name("bonny")
get_name("jack","rose")
get_city("tainan")

#使用as為模組指定別名
from f_name import get_name as gn
gn("bonny")
gn("jack","rose")


##匯入模組中所有函式
from f_name import *
get_name("bonny")
get_city("taipei")







