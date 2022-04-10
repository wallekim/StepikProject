n, m = list(map(int, input().split()))

max_side = max(n, m)
min_side = min(n,m)
k = 0

while min_side >= 1:
    max_side -= min_side
    if min_side > max_side:
        min_side, max_side = max_side, min_side
    k += 1

print(k)
