import sys
def getArea(h, word):
    height = 0
    for i in word:
        if height < h[ord(i) - ord('a')]:
            height = h[ord(i) - ord('a')]
    return len(word) * height
h = list(map(int, input().strip().split(' ')))
word = input().strip()
print (getArea(h, word))

