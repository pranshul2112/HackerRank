n, m = map(int, input().split())
arr = []
for i in range(n):
    a = input()
    arr.append(a)
flag = team = 0

for i in range(n):

    for j in range(i+1, n):

        counter = bin(int(arr[i], 2) | (int(arr[j], 2))).count("1")

        if counter > flag:
            flag = counter
            team = 1
        elif counter == flag:
            team += 1

print(flag)
print(team)
