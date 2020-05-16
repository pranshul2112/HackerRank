
def taumBday(b, w, bc, wc, z):
    if bc > wc and wc + z < bc: #Converting Black Gifts into White
        return b*wc + w*wc + b*z
    elif wc > bc and bc + z < wc: #Converting White Gifts into Black
        return b*bc + w*bc + w*z

    return b*bc + w*wc   



t = int(input())
for t_tr in range (t):
    black, white = map(int, input().split())
    bc, wc, z = map(int, input().split())
    print(taumBday(black, white, bc, wc, z))
