n = int(input())
a = list(map(int, input().rstrip().split()))
lowcount = 0
highcount = 0
low : int = a[0]
high : int = a[0]
for i in range(n-1):
    if a[i] > high:
        highcount += 1
        high = a[i]
    if a[i] < low:
        lowcount += 1
        low = a[i]
if a[n-1] > high:
    highcount += 1
if a[n-1] < low:
    lowcount += 1
print(highcount, lowcount)
