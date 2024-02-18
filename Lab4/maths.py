#1

import math
x = int(input())
print(math.radians(x))

#2

def f(a,b,h):
    trapezoid = ((a+b)/2)*h
    return trapezoid
a = int(input("Enter base1: "))
b = int(input("Enter base2: "))
h = int(input("Enter the height: "))
print(f(a,b,h))

#3

import math
def f(n,a):
    polygon = (n*a**2)/4*math.tan((math.pi)/n)
    return math.ceil(polygon)
n = int(input("Enter the number of sides: "))
a = int(input("Enter the length of a sides: "))
print(f(n,a))

#4

import math
def f(a, b):
    parallelogram = abs(a * b)
    return parallelogram
a = int(input("Enter side1")) 
b = int(input("Enter side2"))
print(f(a,b))