def abc(bill, k, b):
    billtot = 0
    for i in range(len(bill)):
        billtot = billtot + bill[i]
    #print("BEFORE", billtot)
    billanna = (billtot - bill[k]) // 2
    #print("ANNA", billanna)
    #billtot = (billtot - billanna) // 2
    if billanna == b:
        print("Bon Appetit")
    else:
        print(b - billanna)



nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
abc(bill, k, b)
