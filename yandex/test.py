a = str(input())
b = str(input())

sum = 0

for i in set(a):
    sum += b.count(i)
print(sum)
