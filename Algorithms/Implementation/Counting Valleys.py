def count_valley(s, n):
        level = valley = 0
        for i in range(n):
            if s[i] == 'U' or s[i]== 'u':
                level += 1
                if level == 0:
                    valley += 1
            else:
                level -= 1
        print(valley)
n = int(input())
s = input()
count_valley(s, n)

