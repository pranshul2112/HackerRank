def designerPDF(keyboards, drives, b):
    return max([sum([x, y]) for x in keyboards for y in drives if sum([x, y]) <= b] + [-1])


b, n, m = map(int, input().split())
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))
get_money = designerPDF(keyboards, drives, b)
print(get_money)
