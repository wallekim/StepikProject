
n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
b = 1
c = 0
d = n - 1
v = 0
if (n % 2 == 0 or n % 2 == 1) and n != 1:
    for i in range(n // 2):
        for j in range(c, n - 1 - c):
            a[i][j] = b
            b += 1
        for j in range(c, n - 1 - c):
            a[j][d] = b
            b += 1
        for j in range(n - 1 - c, c, -1):
            a[d][j] = b
            b += 1
        for j in range(n - 1 - c, c, -1):
            a[j][v] = b
            b += 1
        c += 1
        d -= 1
        v += 1
    if n % 2 == 1:
        for j in range(n-1, n):
            a[((n - 1) // 2)][((n-1) // 2)] = n ** 2
    for i in a:
        print(*i)
if n == 1:
    print(1)