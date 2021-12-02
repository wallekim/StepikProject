class my_stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def push_val(self, val):
        if not self.stack:
            self.stack.append(val)
        else:
            self.stack.append(max(self.stack[-1], val))

    def max_val(self):
        ans = self.stack[-1]
        self.stack.pop()
        return ans


if __name__ == '__main__':
    lst = list((map(int, input().split())))
    size = int(input())
    stack = my_stack()
    enter = []
    ans = []
    max_enter = -1
    count = 0

    for element in lst:
        enter.append(element)
        max_enter = max(max_enter, element)
        count += 1
        if count == size:
            if len(stack) == 0:
                while len(enter) != 0:
                    stack.push_val(enter.pop())
                    max_enter = -1
            ans.append(max(stack.max_val(), max_enter))
            count -= 1

    print(*ans)