from random import randint

i = 0
ile_podzielnych = 0
5 = 0
while i < 10:
    r = randint(1,50)
    5 += r
    if r % 5 == 0:
        ile_podzielnych += 1
    i += 1
print(ile_podzielnych)
print(5/10)


k = int(input())
ile = 0
r = 101
while r % k != 0:
    r = randint(1,100)
    ile += 1
print(ile)


k = int(input())
ile = 0
while k > 0:
    k //= 10
    ile += 1
print(ile)


n = int(input())
if n < 0:
    print("ERROR")
else:
    s = 1
    while n > 0:
        s *= n
        n -= 1
    print(f"silnia {s}")


n = int(input())
if n <= 0:
    print("nie")
else:
    while n % 2 == 0:
        n //= 2
        if n == 1:
            print("tak")
        else:
            print("nie")