x, y, w, h = map(int, input().split())

# 점에서 직사각형의 네 변까지의 거리 계산6
dist1 = x  # 왼쪽 변까지의 거리
dist2 = w - x  # 오른쪽 변까지의 거리
dist3 = y  # 아래쪽 변까지의 거리
dist4 = h - y  # 위쪽 변까지의 거리

# 네 거리 중 최소값 출력
print(min(dist1, dist2, dist3, dist4))
