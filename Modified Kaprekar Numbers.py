p = int(input())
q = int(input())

result=[]
for i in range(p,q+1,1):
    k = i**2
    right = k % (10 ** len(str(i)))
    left = k // (10 ** len(str(i)))
    if i == int(right)+int(left):
            result.append(i)
 


result= list(set(result))
result.sort()
if len(result) == 0:
    print ('INVALID RANGE')
else:
    print (' '.join([str(i) for i in result]))
