
def chocolateFeast(n, cost, m):
    count = n // cost
    flag = count
    while flag >= m:
        wrap = flag // m
        count += wrap
        flag = flag - (m * wrap) + wrap
    return count


t = int(input())
for t_tr in range(t):
    ncm = list(map(int, input().split()))
    n = ncm[0]
    cost = ncm[1]
    m = ncm[2]
    print(chocolateFeast(n, cost, m))
