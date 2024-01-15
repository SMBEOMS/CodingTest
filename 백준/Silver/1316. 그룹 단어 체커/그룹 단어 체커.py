n = int(input())
result = 0

for _ in range(n):
    word = input()
    if len(word) == len(set(word)): 
        result += 1
    else:
        is_group_word = True
        used_chars = set()
        prev_char = ''
        for char in word:
            if char in used_chars and char != prev_char:
                is_group_word = False
                break
            used_chars.add(char)
            prev_char = char
        if is_group_word:
            result += 1

print(result)
