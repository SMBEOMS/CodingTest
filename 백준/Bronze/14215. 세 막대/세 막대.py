sticks = list(map(int, input().split()))
sticks.sort()

while sticks[2] >= sticks[0] + sticks[1]:
    sticks[2] -= 1

perimeter = sum(sticks)

print(perimeter)