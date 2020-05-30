# Each container contains only balls of the same type.
# No two balls of the same type are located in different containers.
def organiseContainers(arr):
    counter = [0] * len(arr[0])
    for i in arr:
        temp = 0
        for j in i:
            counter[temp] += j
            temp += 1
    temp = 0
    for i in counter:
        flag = False
        for j in arr:
            color = i - j[temp]
            left = sum(j) - j [temp]
            if left == color:
                flag = True
        if flag == False:
            return "Impossible"
        return "Possible"

q = int(input())
for _ in range(q):
    n = int(input())
    arr = []
    for x in range(n):
        a = list(map(int, input().split()))
        arr.append(a)

    print(organiseContainers(arr))

