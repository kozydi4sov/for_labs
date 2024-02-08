def fun(x):
    for i in range(len(x)):
        if x[i] == 3 and x[i+1] == 3:
            return True
    return False
x = input()
lists = [int(i) for i in x.split()]
print(fun(lists))