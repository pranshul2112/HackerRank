
n = int(input())

unsorted = []

for _ in range(n):
        unsorted_item = (input())
        unsorted.append(unsorted_item)


unsorted.sort(key = lambda x: (len(x), x))
for i in unsorted:
    print(i)
