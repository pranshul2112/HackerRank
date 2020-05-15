n = int(input().strip())
a = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
k = 0
for i in range(len(a)):
        count = flag = 0
        while count < m :
            flag +=a[i+count]
            count+=1
        if flag == d:
            k += 1
        if(i + count == len(a)):
            break
print(k)
