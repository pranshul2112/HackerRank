from _collections import defaultdict


def tripletCount(arr, r):

    flag = 0
    dic1, dic2 = defaultdict(int), defaultdict(int) #defauldict doesn't raise KeyError
    for i in reversed(arr):
        if i * r in dic2:
            flag += dic2[i * r]

        if i * r in dic1:
            dic2[i] += dic1[i * r]

        dic1[i] += 1
    return flag


n, r = map(int, input().split()) #n number of terms, r common ratio 
arr = list(map(int, input().split()))
print(tripletCount(arr, r))
