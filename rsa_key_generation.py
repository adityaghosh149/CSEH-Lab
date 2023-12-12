import random
import math


def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("Mod inverse does not exist!")


p = 0
while True:
    p = int(input("Enter a prime value for p : "))
    if is_prime(p):
        break
    else:
        print("p is not prime. Try again!")

q = 0
while True:
    q = int(input("Enter a prime value for q : "))
    if is_prime(q):
        break
    else:
        print("q is not prime. Try again!")


n = p * q

phi_n = (p - 1) * (q - 1)

e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

d = mod_inverse(e, phi_n)

print(f"Public Key : ({e}, {n})")
print(f"Private Key : ({d}, {n})")