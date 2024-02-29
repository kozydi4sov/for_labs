#1

import re
txt = (input())
x = re.findall("ab*", txt)
print(x)

#2

import re
txt = input()
x = re.findall("ab{2,3}", txt)
print(x)

#3

import re 
txt = input()
x = re.findall(r"[a-z]+_[a-z]+", txt)
print(x)

#4
import re
txt = input()
x = re.findall("[A-Z][a-z]+", txt)
print(x)

#5

import re
txt = input()
x = re.findall("a.+b", txt)
print(x)

#6  

import re
x = input()
txt = re.sub("[ ,.]",":",x)
print(txt)

#7

import re
txt = input()
str = txt.split('_')
x = str[0] + ''.join(i.title() for i in str[1:])
print(x)

#8

import re
txt = input()
x = re.findall("[A-Z][^A-Z]*",txt)
print(x)

#9

import re
txt = input()
x = re.findall("[A-Z][^A-Z]*",txt)
slova = ' '.join(x)
print(slova)

#10

import re
txt = input()
x = re.findall(r"[A-Z][a-z0-9]*",txt)
slova = '_'.join(i.lower() for i in x)
print(slova)