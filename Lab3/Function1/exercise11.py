def polindrome(x):
    k = ''.join(reversed(x))
    if x == k:
        return True
    return False

x = input()
if polindrome(x):
    print('da')
else:
    print('net')