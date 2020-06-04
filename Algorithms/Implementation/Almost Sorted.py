from copy import *

def almostSorted(arr):
    n = len(arr)
    test = deepcopy(arr)
    test.sort()

    if test == arr:
        print("yes")
        return

    left = right = n - 1
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            left = i
            break
    for i in range(n - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            right = i
            break

    temp = deepcopy(arr)
    temp[left], temp[right] = temp[right], temp[left]

    if temp == test:
        print("yes")
        print("swap", left + 1, right + 1)
        return

    temp = deepcopy(arr)
    temp = temp[:left] + temp[left: right + 1][::-1] + temp[right + 1:]

    if temp == test:
        print("yes")
        print("reverse", left + 1, right + 1)
        return 
    
    print("no")
    return 
        

n = int(input())

arr = list(map(int, input().rstrip().split()))

almostSorted(arr)
