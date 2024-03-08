n = int(input())

lst = []  
for _ in range(n):
    x, y = map(int, input().split())  # 괄호 제거
    lst.append([x, y])

lst.sort(key=lambda point: (point[1], point[0]))  

for x, y in lst:
    print(x, y)
