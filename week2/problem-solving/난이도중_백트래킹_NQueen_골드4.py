# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

rotated = []
# TODO: n x n 크기의 새로운 배열을 생성하세요 (0으로 초기화)
for x in range(3):
    rotated.append([])
    for y in range(3):
        rotated[x].append(0)

print(rotated)