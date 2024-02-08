def rev(x):
    sen = x.split()
    result = ' '.join(reversed(sen))
    return result
sen = input()
print(rev(sen))