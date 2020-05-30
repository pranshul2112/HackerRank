def mincost(string):
    n = len(string)
    res = 0
    
    for i in range(n // 2):
        x = ord(string[i])
        y = ord(string[n - i - 1])
        
        if x == y:
            continue    
      
        res += abs(x - y)
            
    return res


n = int(input())
for _ in range(n):
    string = input()
    print(mincost(string))
    
