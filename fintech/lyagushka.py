from collections import defaultdict
from math import inf

if __name__ == '__main__':
    # n = 3
    # a_i = {
    #     0: 2,  # на расстоянии 2 от вершины он может прыгнуть на 2
    #     1: 2,  # на расстоянии 1 от вершины он может прыгнуть на 2
    #     2: 0,  # на самой вершине он не может прыгать
    # }
    # b_i = {
    #     0: 0,  # на расстоянии 2(в самом низу) от вершины его не сносит
    #     1: 1,  # на расстоянии 1(на высоте 1) от вершины сносит на 1 клетку
    #     2: 1,  # на расстоянии 0(на высоте 2) от вершины снесет на 1 клетку
    #     3: 0
    # }
    a_i = {}
    b_i = {}
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    b = list(map(int, input().split()))
    b.reverse()
    for i in range(len(a)):
        a_i[i] = int(a[i])
    for i in range(len(b)):
        b_i[i] = int(b[i])
    b_i[n] = 0
    ways = {
        0: 0
    }

    for _from in range(n):
        for jump in range(1, a_i[_from] + 1):
            ways[_from + jump - b_i[_from + jump]] = min(
                ways.get(_from + jump - b_i[_from + jump], inf),
                ways.get(_from, inf) + 1
            )
    if ways[n] == inf:
        print(-1)
    else:
        print(ways[n])