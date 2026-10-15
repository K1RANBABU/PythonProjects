def find_gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a
print(find_gcd(48,18))