gas = list(map(int, input().split()))
distance = list(map(int, input().split()))


def zep(gas, distance):
    start = 0
    total = 0
    tank = 0
    for i in range(len(gas)):
        tank += gas[i] - distance[i]
        if tank < 0:
            start = i + 1
            if i >= len(gas):
                i = 0
            total += tank
            tank = 0
    if total + tank >= 0:
        for i in range(start, len(gas)):
            tank += gas[i] - distance[i]
            if tank < 0:
                return -1
        for i in range(start):
            tank += gas[i] - distance[i]
            if tank < 0:
                return -1
        return start
    else:
        return -1


print(zep(gas, distance))
