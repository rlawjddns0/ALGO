n, m, a = map(int, input().split())

if n > a or m > a:
    if n == 1 and m == 1:
        print(1)
    elif n % a == 0 and m % a == 0:
        print(n // a * m // a)
    elif n % a != 0 and m % a == 0 or n % a == 0 and m % a != 0:
        print((n // a) * ((m // a) + 1))
    else:
        print(((n // a) + 1) * ((m // a) + 1))
else:
    print(1)