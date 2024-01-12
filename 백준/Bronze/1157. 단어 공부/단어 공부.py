word = input().upper()
unique_letters = list(set(word))

cnt_list = []
for x in unique_letters:
    cnt = word.count(x)
    cnt_list.append(cnt)  # Count each letter's occurrence and add it to the list

if cnt_list.count(max(cnt_list)) > 1:  # Check if the highest count is more than one
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))  # Find the index of the most frequent letter
    print(unique_letters[max_index])
