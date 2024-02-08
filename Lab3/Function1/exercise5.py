from itertools import permutations

def allperm(string):
    charlist = list(string)
    perm = permutations(charlist, len(charlist))
    result = list(perm)
    return result
x = input()
print(allperm(x))