def wallheight(current, previous):
    return abs(current - previous)


def surfacearea(height, width, area):
    ans = 2 * height * width
    for i in range(height):
        for j in range(width):
            up = left = 0

            if i > 0:
                up = area[i - 1][j]

            if j > 0:
                left = area[i][j - 1]
                
            ans += wallheight(area[i][j], up) + wallheight(area[i][j], left)

            if i == height - 1:
                ans += area[i][j]
                
            if j == width - 1:
                ans += area[i][j]

    return ans


height, width = map(int, input().split())
area = []
for i in range(height):
    h = list(map(int, input().split()))
    area.append(h)
print(surfacearea(height, width, area))
