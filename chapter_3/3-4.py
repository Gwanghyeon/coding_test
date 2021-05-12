n, k = map(int, input().split())

num = 0

while True:
    if n % k == 0:
        n //= k
        num += 1
    else:
        n -= 1
        num += 1
    if n == 1:
        break

print(num)

# From book

n, k = map(int, input().split())

num = 0

while true:
    target = (n//k)*k
    num += (n-target)

    n = target
    if n < k:
        break
    n //= k
    num += 1

num += n-1

print(num)
