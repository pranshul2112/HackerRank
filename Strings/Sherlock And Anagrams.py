
def anagram(s):
    n = len(s)
    res = 0
    for i in range(1, n):
        dic = {}
        for j in range(n - i + 1):
            sub_string = ''.join(sorted(s[j:j + i]))
            if sub_string not in dic:
                dic[sub_string] = 1
            else:
                dic[sub_string] += 1
            res += dic[sub_string] - 1
    return res


t = int(input())
for t_tr in range(t):
    s = input()
    s = list(s)
    print(anagram(s))
