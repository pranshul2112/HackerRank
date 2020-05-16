
def beautifultriplets(arr, n, d):
    count =  0
    for i in range(n):
        if arr[i] + d in arr and arr[i] + (2 * d) in arr :
                count += 1
    return count


nd = list(map(int, input().split()))
n = nd[0]
d = nd[1]
arr = list(map(int, input().rstrip().split()))
res = beautifultriplets(arr, n, d)
print(res)
