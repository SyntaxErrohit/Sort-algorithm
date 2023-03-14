l = [5, 6, 3, 9, 4, 2, 7, 8]

for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
    
print(l)