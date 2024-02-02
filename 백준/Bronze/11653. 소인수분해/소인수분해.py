num = int(input())

start = 2
while num > 1:
    if num % start == 0:
        print(start)
        num //= start
    else:
        start += 1