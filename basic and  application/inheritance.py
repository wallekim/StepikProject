import logging
from collections import defaultdict

parents = defaultdict(list)


def check_inheritance(val_A, val_B):
    notPassedTop = []
    lst = parents[val_B]
    if val_A == val_B:
        return 'Yes'
    for top in lst:
        if top == val_A:
            return 'Yes'
        else:
            notPassedTop.append(top)
    for _top in notPassedTop:
        if check_inheritance(val_A, _top) != 'No':
            return check_inheritance(val_A, _top)
    return 'No'


for i in range(int(input())):
    s = input().split(':')

    if len(s) > 1:
        child = s[1].split()
        for j in range(len(child)):
            parents[s[0].strip()].append(child[j].strip())
    else:
        parents[s[0]].append('object')


for i in range(int(input())):
    par, child = map(str, input().split())
    print(check_inheritance(par, child))
