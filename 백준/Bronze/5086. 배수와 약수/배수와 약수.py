while True:
    a, b = map(int, input().split())

    # 입력 종료 조건
    if a == 0 and b == 0:
        break

    # 약수와 배수 관계 판별
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")
