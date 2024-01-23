N = int(input())

# 중앙의 1을 제외한 계층(layer) 수
layer = 1
# 현재 계층의 최대 방 번호
max_room_number = 1

while N > max_room_number:
    max_room_number += 6 * layer  # 각 계층은 이전 계층보다 방이 6개씩 더 많음
    layer += 1

print(layer)
