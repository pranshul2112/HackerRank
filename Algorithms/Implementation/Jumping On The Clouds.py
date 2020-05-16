def JumpingOnTheClouds(arr):
    count = i = 0
 
    while i < (n - 1):
        if i + 2 <= n - 1 and a[i + 2] == 0:
            count += 1
            i += 2
        elif a[i + 1] == 0:
            count += 1
            i += 1

    return count


n = int(input())
arr = list(map(int, input().rstrip().split()))

print(JumpingOnTheClouds(arr))
