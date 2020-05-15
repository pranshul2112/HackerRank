
def kangaroo(x1, v1, x2, v2):
    if v1 <= v2 or (x2 - x1) % (v1 - v2) != 0:
        print("NO")
    else:
        print("YES")
        

x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
kangaroo(x1, v1, x2, v2)

    
