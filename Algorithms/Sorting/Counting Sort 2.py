
n = int(input())
arr = list(map(int, input().split()))

arr.sort()
print(" ".join(str(x) for x in  arr))
