import itertools


def next_computation(s):
    return computation(s, lambda x, y: x <= y)


def prev_computation(s):
    return computation(s, lambda x, y: x >= y)


def computation(s, comparator):
    if type(s) != list:
        raise Exception("permutation's parameter must be a list")

    n = len(s)
    i = n - 1

    while i > 0 and comparator(s[i], s[i - 1]):
        i -= 1
    if i <= 0:
        return False

    j = n - 1
    while comparator(s[j], s[i - 1]):
        j -= 1
    s[i - 1], s[j] = s[j], s[i - 1]
    s[i:] = s[n - 1: i - 1: -1]
    return True


t = int(input())
for t_tr in range(t):
    s = input()
    s = list(s)
    if next_computation(s):
        print(''.join(s))
    else:
        print("no answer")
