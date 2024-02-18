#1

def square_generator(n):
    for i in range(n+1):
        yield i**2
n = int(input("Enter n: "))
print(' '.join(map(str, square_generator(n))))

#2

def even_numbers(n):
    for i in range(n+1):
        if i%2==0:
            yield i
n = int(input("Enter n: "))
print(','.join(map(str, even_numbers(n))))

#3

def f(n,n1):
    for i in range(n,n1+1):
        if i%3==0 and i%4==0:
            yield i
n = int(input("Enter n: "))
n1 = int(input("Enter n1: "))
print(' '.join(map(str, f(n,n1))))

#4

def square_generator(n,n1):
    for i in range(n,n1+1):
        yield i**2
n = int(input("Enter n: "))
n1 = int(input("Enter n1: "))
print(' '.join(map(str, square_generator(n,n1))))

#5

def square_generator(n):
    for i in range(n,-1,-1):
        yield i
n = int(input("Enter n: "))
print(' '.join(map(str, square_generator(n))))