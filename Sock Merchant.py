
def SockMerchant(arr):
    flag = 0
    arr.sort()
   
    i = 0
    while i < n - 1:

        if arr[i] == arr[i + 1]:
            flag += 1
            i += 2
        else:
            i += 1
    return flag
    
    
n = int(input())
arr = list(map(int, input().rstrip().split()))
print(SockMerchant(arr))
