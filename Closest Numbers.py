n = int(input())
arr = list(map(int, input().split()))
arr.sort()
k = arr[1] - arr[0]
a = [arr[0], arr[1]]

for i in range(n - 1):
    if arr[i + 1] - arr[i] < k:
        a = []
        a.append(arr[i])
        a.append(arr[i + 1])
        k = arr[i+1] - arr[i]
    elif arr[i + 1] - arr[i] == k:
        a.append(arr[i])
        a.append(arr[i+1])
        
print(*a)
