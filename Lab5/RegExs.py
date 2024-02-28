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