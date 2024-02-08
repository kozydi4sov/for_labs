def histogram(x):
    result = []
    for i in range(len(x)):
        k = ''
        for j in range(int(x[i])):
            k += '*'
        print(k)

x = input()
lists = [i for i in x.split()]
histogram(lists)