
n = int(input())

arr = list(map(int, input().split()))

print(" ".join(str(x) for x in sorted(arr)))
