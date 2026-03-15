# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630

def divide_conquer(x, y, size):
    result = ()
    white = []
    blue = []

    if color_check(x, y, size) == 1:
        if x == 0:
            white.append(0)
        elif x == 1:
            blue.append(1)

        result = (white, blue)
        return result
    else:
        return divide_conquer(x, y, size//2)
    
def color_check(x, y, size):
    first = paper[x][y]

    for i in range(x, x+size)
        