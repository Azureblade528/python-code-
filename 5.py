def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


number = int(input())
if is_prime(number):
    print("Prime")
else:
    print("Not Prime")
