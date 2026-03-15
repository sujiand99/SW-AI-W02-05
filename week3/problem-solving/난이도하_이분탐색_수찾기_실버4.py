# # 이분탐색 - 수 찾기 (백준 실버4)
# # 문제 링크: https://www.acmicpc.net/problem/1920


# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# arr = list(map(int, input().split()))
# A.sort()

# for num in arr:
#     lt, rt = 0, N-1
#     isExist = False

#     while lt <= rt:
#         mid = (lt + rt)//2
#         if num == A[mid]:
#             isExist = True
#             print(1)
#             break
#         elif num > A[mid]:
#             lt = mid + 1
#         else:
#             rt = mid - 1
    
#     if not isExist:
#         print(0)

# import sys
      
# stack = []
    
# root = sys.stdin.readline().strip().split()

# print(root)

# for i in range(len(root)):
#     stack.append(root[i])
    
#     if stack[-i] == "/":
#         continue
#     if stack[-i] == ".":
#         stack.pop()


# if root[-1] == "/":
#     root.pop()
#     print(root)


cmd_list = input().split("/")
print(cmd_list)
path = []

for cmd in cmd_list:
    if cmd == "" or cmd == ".":
        continue

    elif cmd == "..":
        if path:
            path.pop()
    else:
        path.append(cmd)

print("/"+"/".join(path))
