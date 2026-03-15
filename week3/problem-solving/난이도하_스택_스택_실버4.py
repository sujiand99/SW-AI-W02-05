# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

import sys
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == "push": #정수 X를 스택에 넣는 연산
        stack.append(command[1])

    elif command[0] == "pop":
        if len(stack) == 0: #만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력
            print(-1)
        else:
            print(stack.pop()) #스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력

    elif command[0] == "size": #스택에 들어있는 정수의 개수를 출력
        print(len(stack))

    elif command[0] == "empty":
        if len(stack) == 0: #스택이 비어있으면 1
            print(1)
        else: #아니면 0을 출력
            print(0)

    elif command[0] == "top":
        if len(stack) == 0: #만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력
            print(-1)
        else:
            print(stack[-1]) #아니면 0을 출력