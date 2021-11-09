from collections import defaultdict

parents = defaultdict(list)


def check_inheritance(start, end):
    par = parents[start]
    notPassedTop = []
    if start == end:
        return True

    for top in par:
        if top == end:
            return True
        else:
            notPassedTop.append(top)

    for _top in notPassedTop:
        if check_inheritance(_top, end):
            return check_inheritance(_top, end)

    return False


for i in range(int(input())):

    s = input().split(':')
    if len(s) > 1:
        child = s[1].split()
        for j in range(len(child)):
            parents[s[0].strip()].append(child[j].strip())
    else:
        parents[s[0]]

all_child = []
ans = []
out = []

for i in range(int(input())):

    child = input()
    all_child.append(child)

    for value in all_child:
        ans = check_inheritance(child, value)
        if ans and value != child and child not in out:
            out.append(child)

for value in out:
    print(value)
