num = int(input())

x_coords = []
y_coords = []

for _ in range(num):
    x, y = map(int, input().split())  
    x_coords.append(x)
    y_coords.append(y)


MAX_x = max(x_coords)
Min_x = min(x_coords)

Max_y = max(y_coords)
Min_y = min(y_coords)


width = MAX_x - Min_x
height = Max_y - Min_y


print(width * height)
