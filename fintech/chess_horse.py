from collections import defaultdict


if __name__ == '__main__':
    # target = (4, 1)
    inp_lst = input().split()
    target = (int(inp_lst[0]), int(inp_lst[1]))

    def solve():
        prev_layer = {
            (1, 1): 1
        }
        current_layer = []
        while target not in prev_layer.keys():
            current_layer = defaultdict(int)
            for point in prev_layer:
                current_layer[(point[0]+1, point[1]+2)] += prev_layer[point]
                current_layer[(point[0]+2, point[1]+1)] += prev_layer[point]
                if point[0] + point[1] > target[0] + target[1]:
                    return prev_layer[target]
            prev_layer = current_layer
        return prev_layer[target]

    ans = solve()
    if ans == 0:
        print(1)
    else:
        print(ans)

# if point[0] + point[1] > target[0] + target[1]:
#     return prev_layer[target]
