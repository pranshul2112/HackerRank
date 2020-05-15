def abc(keyboards, drives, b):
    return max([sum([x, y]) for x in keyboards for y in drives if sum([x, y]) <= b] + [-1])
    
bnm = input().split()
b = int(bnm[0])
n = int(bnm[1])
m = int(bnm[2])
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
get_money = abc(keyboards, drives, b)
print(get_money)
