
def abc(x, y, z):
    cata = abs(z-x)
    catb = abs(z -y)
    if cata < catb:
        print("Cat A")
    elif cata > catb:
        print("Cat B")
    else:
        print("Mouse C")
        
n = int(input())        
for i in range(n):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    abc(x, y, z)
