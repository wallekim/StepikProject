from sys import stdin
text = stdin.read()

# text = '''
# 2
# 20
# 004
# 66
# '''

text = text.split('\n')

texNval = []

for value in text:
    if value != '':
        val = tuple(value)
        texNval.append(val)

texNval.sort(key= lambda texNval: texNval[0])
prev_value = texNval[0][0]
for i, val in enumerate(texNval):
    if val[-1] == '0' and prev_value == val[0]:
        texNval[i], texNval[i-1] = texNval[i-1], texNval[i]
    prev_value = val[0]
texNval.reverse()

s = ''

for i in texNval:
    for j in i:
        s += j


print(s)
