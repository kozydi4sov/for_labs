#ex1

import os 
x = input()
print(os.listdir(x))
for i in os.listdir(x):
    if os.path.isdir(x):
        print(i)
for j in os.listdir(x):
    if os.path.isfile(x):
        print(i)

#ex2

import os 
x = input()
if os.path.exist(x):
    print('yes')
if os.acces(x, os.R_OK):
    print('yes')
if os.acces(x, os.W_OK):
    print('yes')
if os.acces(x, os.X_OK):
    print('yes')

#ex3

import os 
x = input()
if os.path.exist(x):
    name = os.path.basename(x)
    name2 = os.path.dirname(x)
print(name, name2)

#ex4

import os 
x = input()
f = open(x, 'r') as file
line_sum = sum(1 for line in file)
print(line_sum)

#ex5

import os 
x = input()
y = ['a', 'b', 'c']
f = open(x, 'w')
f.write(y)
f.close()
f.open(x, 'r')
print(f.read(x))

#ex6

import os 
x = getcwd()
for i in range(ord('A'), ord('Z') + 1):
    fname = chr(i) + '.txt'
    f = open(fname)

#ex7

import os 
x = input()
f = open(x, 'r')
y = f.read(x)
f.close()
d = open('copy', 'w')
d.write(y)
d.close()

#ex8

import os 
x = input()
if os.path.exist(x):
    os.remove(x)