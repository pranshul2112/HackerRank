
n = int(input())
score = list(map(int, input().split()))
m = int(input())
alice = list(map(int, input().split()))
leader = sorted(set(score), reverse=True)
l = len(leader)
for a in alice:
    while (l > 0) and (a >= leader[l-1]):
        l -= 1
    print(l+1)
