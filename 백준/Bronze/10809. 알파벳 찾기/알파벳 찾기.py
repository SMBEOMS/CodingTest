# 알파벳 소문자로 이루어진 문자열 입력
s = input()

# 알파벳 소문자를 저장할 리스트 초기화
alphabet_positions = [-1] * 26

# 문자열을 순회하면서 각 알파벳의 첫 등장 위치 찾기
for i in range(len(s)):
    idx = ord(s[i]) - ord('a')
    if alphabet_positions[idx] == -1:
        alphabet_positions[idx] = i

# 결과 출력
for position in alphabet_positions:
    print(position, end=' ')
