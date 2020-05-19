def insertionSort(arr):
    count = 0
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1

        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            count += 1

        arr[j + 1] = temp
    return count 
    
    
n = int(input())
arr = list(map(int, input().split()))
print(insertionSort(arr))
