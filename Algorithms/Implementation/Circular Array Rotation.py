
n, k, q = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))

rotationfactor = k % n

for i in range(q):
    m = int(input())
    
    print(arr[(n - rotationfactor + m) % n])
