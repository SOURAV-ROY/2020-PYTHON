import math

user_num = int(input('Upper Limit For Prime: '))


def is_prime(num):
    for p in range(2, int(math.sqrt(num) + 1)):
        if num % p == 0:
            return False
    return True


for i in range(1, user_num + 1):
    if is_prime(i):
        print(i)
