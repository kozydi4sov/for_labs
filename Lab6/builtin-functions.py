#ex1 

lists = []
while True:
    x = input()
    if not x:
        break   
    else:
        lists.append(x)
y = 1
for i in range(len(lists)):
    y = y * int(lists[i])
print(y)

#ex2

s = input()
u = 0
l = 0
for i in range(len(s)):
    x = s[i]
    if x.isupper():
        u += 1 
    else:
        l += 1 
print(u, l)

#ex3

s = input()
x = ''.join(reversed(s))
if x == s:
    print('yes')
else:
    print('no')

#ex4

import math
import time 
x = int(input())
y = math.sqrt(x)
time.sleep(2.123)
print(y)

#ex5

t = []
i = 0
while True:
    x = input()
    if not x:
        break
    else:
        t.append(x)
y = all(int(t[i]) == True for i in range(len(t)))
print(y)