
def hourglass(arr):
    max_sum = -float('inf')
    for row in range(4):
        for col in range(4):
            max_sum = max(arr[row][col] + arr[row][col + 1] + arr[row][col + 2] +
                      arr[row + 1][col + 1] +
                      arr[row + 2][col] + arr[row + 2][col + 1] + arr[row + 2][col + 2],
                      max_sum)
    return max_sum
    
arr = []
for _ in range(6):
    a = list(map(int, input().rstrip().split()))
    arr.append(a)

res = hourglass(arr)
print(res)
