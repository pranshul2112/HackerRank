def abc(a):
    flag = 0
    a.sort()
    i = 0
    while i < n-1:

        if a[i] == a[i + 1]:
            flag += 1
            i += 2
        else:
            i += 1
    print(flag)
n = int(input())
a = list(map(int, input().rstrip().split()))
abc(a)
