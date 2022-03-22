k = [[1, 2], [4], [5, 6, 2], [1, 2], [3], [4]]

new_k = []

for elem in k:
    if elem not in new_k:
        new_k.append(elem)
        
k = new_k
print(k)   

l1 = [1, 2, 2, 4]
l2 = [2, 5, 5, 5, 6]   

new  = set(l2) - set(l1)

l = l1 + list(new)

print(l)