
def halloweenSale(p, d, m, s):
    flag = 0
    while s >= p:
        
        flag += 1
        s -= p
        p = max(p - d, m)
    
    
    return flag
p, d, m, s = map(int, input().split())
print(halloweenSale(p, d, m, s))
