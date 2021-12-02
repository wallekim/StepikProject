size, quantity = map(int, input().split())

queue = []
all_depature = []
all_arrival = []


for i in range(quantity):
    arrival, duration = map(int, input().split())
    if len(queue) < size:
        if i == 0:
            all_depature.append(arrival)
        print(max(all_depature[-1], arrival))
        queue.append(duration)
        all_arrival.append(arrival)
        all_depature.append(max(all_depature[-1], arrival) + duration)
    else:
        if arrival >= queue[0] + max(all_depature[0], all_arrival[0]):
            queue.pop(0)
            all_arrival.pop(0)
            all_depature.pop(0)
            print(max(all_depature[-1], arrival))
            queue.append(duration)
            all_arrival.append(arrival)
            all_depature.append(max(all_depature[-1], arrival) + duration)
        else:
            print(-1)

