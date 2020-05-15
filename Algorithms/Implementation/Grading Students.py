a = []
n = int(input())
for i in range(n):
    m = int(input())
    a.append(m)
for i in range(n):
    if a[i] <= 37:
        print(a[i])
    else:
            c = a[i] % 5

            if c >= 3:
                a[i] += 5 - c
                print(a[i])
            else:
                print(a[i])
