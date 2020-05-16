from bisect import insort, bisect

def maximumSum(arr, m):
    gsum = lsum = 0
    psum = []

    for i in range(len(arr)):
        lsum = (lsum + arr[i]) % m
        pos = bisect(psum, lsum)
        
        x = 0 if pos == i else psum[pos]
        
        gsum = max(gsum, (lsum - x + m) % m)
        
        insort(psum, lsum)
    
    return gsum


q = int(input())
for i in range(q):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(maximumSum(arr, m))
