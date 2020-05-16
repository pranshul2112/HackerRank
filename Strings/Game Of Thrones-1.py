# The given program is to check if a palindrome string can be formed from a given string.

def gameofthrones(s):
    n = len(s)
    dic = {}
    odd = 0
    for i in s:
        dic[i] = dic.get(i, 0) + 1 # Gets occurences of elements
   
    for i in dic:
        if dic[i] % 2 != 0:
            odd += 1
    if (odd == 1 and n % 2 == 0) or odd > 1:
        return "NO"

    else:
        return "YES"


s = input()
print(gameofthrones(s))
