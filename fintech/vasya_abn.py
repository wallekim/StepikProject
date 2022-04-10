a, b, n = list(map(int, input().split()))

if n <= (a-b) and (a+b) % 2 == 0 and (a-b) % 2 == 0:
    print('Yes')
else:
    print('No')