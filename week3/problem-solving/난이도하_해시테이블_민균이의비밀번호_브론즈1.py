# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

# password = {
#     'las' : 1,
#     'god' : 2,
#     'psala' : 3,
#     'sal' : 4
# }

import sys
input = sys.stdin.readline
N = int(input())
text_file = {}

for _ in range(N):
    password = input().strip()
    text_file[password] = True
# words_dict = {input().strip(): 1 for _ in range(N)}

for word in text_file:
    if word[::-1] in text_file:
    # [::-1]는 그냥 단순히 글자를 뒤집는거
        length = len(word)
        middle_char = word[length//2]
        print(f"{length} {middle_char}")
        break
    