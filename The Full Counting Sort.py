
n = int(input())
strings = ["" for j in range(n)]
for i in range(n):
    x, s = map(str, input().split())
    x = int(x)
    if i < n / 2:
        s = "-"
    strings[x] += s + " "

print("".join(str(x) for x in strings))
