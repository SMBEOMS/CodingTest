N = int(input())  
words = set()  

for _ in range(N):
    words.add(input())  


words = list(words)


def sort_criteria(word):
    return len(word), word


words.sort(key=sort_criteria)  
for word in words:
    print(word)
