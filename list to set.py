nums=[1, 2, 3, 2,9,9,9,09999999, 4, 5, 1, 6, 3]
s=[]
for i in nums:
    if i not in s:
        s.append(i)
print(s)  #converts the sorted list to set



