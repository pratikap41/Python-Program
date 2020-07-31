n = int(input())
l = []
for i in range(n):
    word = input()
    l.append(word)

print(len(set(l)))
str1 = ' '.join(l)
for i in l:
    print(str1.count(i), end=' ')

