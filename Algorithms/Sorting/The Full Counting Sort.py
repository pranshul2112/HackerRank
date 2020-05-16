
n = int(input())
strings = ["" for i in range(n)]
for i in range(n):
    x, s = map(str, input().split())
    x = int(x)
    if i < n / 2:
        s = "-"
    strings[x] += s + " "

print("".join(str(i) for i in strings))
