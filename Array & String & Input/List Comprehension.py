'''List Comprehension'''

# in-place construction
arr1 = [i for i in range(10)]


# you can use if to filter the elements
arr2 = [x for x in arr1 if x % 2 == 0]


# you can use as many conditions as you want!
arr3 = [x for x in arr1 if x >= 3 and x % 2]
                                    #( x % 2 不等於0的數)    

# use nested for loops to make everyone dizzy XD
arr4 = [(x, y) for x in range(3) for y in range(4)]


print(arr1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr2) #[0, 2, 4, 6, 8]
print(arr3) #[3, 5, 7, 9]
print(arr4) # [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1),
            #  (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]


'''List Comprehension的效率'''
#兩次創造List的前後計時，以算出執行所需時間。
import time

arr1 = []
s = time.time()
for i in range(int(1e+6)):
    arr1.append(i)
print('took {} secs'.format(round(time.time() - s, 3)))

s = time.time()
arr2 = [i for i in range(int(1e+6))]
print('took {} secs'.format(round(time.time() - s, 3)))

'''引入模組'''
'''
# standard import
import time

# import and give alias
import random as rd

# precise imoprt
from pathlib import Path

# useless statement
from datetime import *
'''

'''List Comprehension背後的原理'''

# what if we don't assign comprehension to list?
comp = (i for i in range(10))
print(comp)
print(type(comp))

arr1 = list(comp)
arr2 = list(comp)
arr3 = [comp]
print(arr1)
print(arr2)
print(arr3)


'''test'''

### anser1
arrA = [i for i in range(1, 21) if i%2!=0]
arrB = [i for i in range(1, 21) if i%2==0]

for index in range(len(arrA)):
    print(str(arrA[index])+" <--> "+str(arrB[index]))


### anser2
arra = [i for i in range(1, 21,2) ]
arrb = [i for i in range(2, 21,2) ]

for o, e in zip(arra, arrb):
    print(o, e, sep=' <---> ')

## zip :會接受不限個數的序列容器，並把他們合而為一，成為一個超大的序列容器
## sep : 不以空白隔開



m=[x*y for x in range(1,10)for y in range(1,10)]
print(m)


m = [x for x in range(1,101)if x%2!=0 and x%3!=0 and x%5!=0]
print(m)



##Dictionary Comprehension

dict_e = {x:x%2==0 for x in range(1,101)}
print(dict_e)
