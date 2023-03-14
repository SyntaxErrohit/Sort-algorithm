l = [5, 6, 3, 9, 4, 2, 7, 8]

for i in range(len(l)):
    j = i
    while j > 0 and l[j-1] > l[j]:
        l[j-1], l[j] = l[j], l[j-1]
        j -= 1

print(l)
