def prime(x):
    if x > 3:
        a = int(math.sqrt(x))
        for i in range(2, a  + 1):
            if x % i == 0:
                return False
    else:
        return True
    return True
list1 = []
while True:
    x = int(input())
    if not x:
            break
    else:
        if prime(x):
            list1.append(x)
for i in range(len(list1)):
    print(list1[i])