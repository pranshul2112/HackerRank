
import math


def squarefinder(a, b):

    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1


t = int(input())

for t_tr in range(t):
    
    a, b = map(int, input().split())
    print(squarefinder(a, b))
