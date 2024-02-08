def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num** 0.5) + 1):
        if num % i == 0:
            return False
        return True
    
input_numbers =  input("Enter a list of numbers separated by commas: ")
numbers = [int(x) for x in input_numbers.split(',')]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Original list:", numbers)
print("Prime numbers:", prime_numbers)