import sys


def miniumdistance(arr, n):
    flag = sys.maxsize
    dic = {}
    for i in range(n):
        if arr[i] not in dic:
            dic[arr[i]] = i
        else:
            flag = min(flag, i - dic[arr[i]])
            dic[arr[i]] = i
    return flag if flag < sys.maxsize else -1


n = int(input())
arr = list(map(int, input().split()))
res = miniumdistance(arr, n)
print(res)
