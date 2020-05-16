
def appendAndDelete(s, t, k):

    commonlen = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            commonlen += 1
        else:
            break

    if len(s) + len(t) - 2 * commonlen > k:
        return False
    elif (len(s) + len(t) - 2 * commonlen) % 2 == k % 2:
        return True
    elif len(s) + len(t) < k:
        return True
    else:
        return False

        
s = input()
t = input()
k = int(input())
if appendAndDelete(s, t, k):
    print("Yes")
else:
    print("No")
