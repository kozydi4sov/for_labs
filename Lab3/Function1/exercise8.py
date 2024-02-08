def fun(x):
    for i in range(len(x)):
        if x[i] == 0 and x[i+1] == 0 and x[i+2] == 7:
            return True
    return False
x = input()
lists = [int(i) for i in x.split()]
print(fun(lists))