import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numberOfSwaps = 0
def swap(j):    
    t = a[j]
    a[j] = a[j + 1]
    a[j + 1] = t

for i in range(0,n):    
    for j in range(0, n-1):
        if a[j] > a[j + 1]:
            swap(j)
            numberOfSwaps = numberOfSwaps + 1

    if numberOfSwaps == 0:
        break       


print("Array is sorted in {} swaps.".format(numberOfSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))