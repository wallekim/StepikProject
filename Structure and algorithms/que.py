size, quantity = map(int, input().split())

queue = []
prev_depature = 0
first_arrival = []

for i in range(quantity):
    arrival, duration = map(int, input().split())
    if len(queue) < size:
        if i == 0:
            prev_depature = arrival
        print(prev_depature)
        queue.append(duration)
        first_arrival.append(arrival)
        prev_depature += duration
    else:
        if arrival >= queue[0] + first_arrival[0]:
            diff = arrival - prev_depature
            queue.pop(0)
            first_arrival.pop(0)
            print(prev_depature + diff)
            queue.append(duration)
            first_arrival.append(arrival)
            prev_depature += duration
        else:
            print(-1)
