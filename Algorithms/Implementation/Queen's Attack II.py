
def queensAttack(r_q, c_q, obs):
    moves = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            x = r_q + i
            y = c_q + j

            while x >= 1 and y >= 1 and x <= n and y <= n and (x, y) not in obs:
                moves += 1
                x += i
                y += j

    return moves

n, k = map(int, input().split())
r_q, c_q = map(int, input().split())
obstacle = set()
for i in range(k):
    a, b = map(int, input().split())
    obstacle.add((a, b))

print(queensAttack(r_q, c_q, obstacle))
