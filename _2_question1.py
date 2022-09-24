# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
l=[(2,5),(1,2),(4,4),(2,3),(2,1)]
for j in range(1,2):
    for i in range(0,5):
        for k in range(i+1,5):
            if l[i][j] > l[k][j]:
                temp=l[i]
                l[i]=l[k]
                l[k]=temp
print(l)