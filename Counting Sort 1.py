def solution(data, n):
    dic = {}

    for i in data:
        dic[i] = dic.get(i, 0) + 1

    for key in range(100):
            if key in dic:
                print(dic[key], end=' ')
            else:
                print(0, end=' ')

    return None

n = int(input())
data = list(map(int, input().split()))
solution(data, n)
