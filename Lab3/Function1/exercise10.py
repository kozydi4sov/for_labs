def uni(x):
    lists = []
    k = 1
    for i in range(len(x)):
        k = 1
        for j in range(len(x)):
            if i != j:
                if x[i] == x[j]:
                    break
                else:
                    k += 1
        if k == len(x):
            lists.append(x[i])
    return lists
x = input()
lists = [str(a) for a in x.split()]
print(uni(lists))