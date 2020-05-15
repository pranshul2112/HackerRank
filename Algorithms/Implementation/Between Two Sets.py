import math
def abc(arr, brr):
    lcm_num = arr[0]
    gcd_num = brr[0]
    if len(arr) > 1:
        for i in range(len(arr)):
            lcm_num = (lcm_num * arr[i])//math.gcd(lcm_num, arr[i])
    if len(brr) > 1:
        for i in range(len(brr)):
            gcd_num = math.gcd(gcd_num, brr[i])
    flag = 0
    for i in range(lcm_num, gcd_num + 1, lcm_num):
        if math.gcd(gcd_num, i) == i:
            flag += 1
    return flag
