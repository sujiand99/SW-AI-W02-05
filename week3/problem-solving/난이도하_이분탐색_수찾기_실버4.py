# # 이분탐색 - 수 찾기 (백준 실버4)
# # 문제 링크: https://www.acmicpc.net/problem/1920

#arr2의 각각의 수가 arr1에 존재하면 1 존재하지 않으면 0

def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2

        if arr[mid]==target:
            return 1
        elif arr[mid]<target:
            left = mid + 1
        elif arr[mid]>target:
            right = mid - 1
    
    return 0


N = int(input())
arr1 = [int(x) for x in input().split()]

N = int(input())
arr2 = [int(x) for x in input().split()]

arr1.sort()
lst = []

for x in arr2:
    result = binary_search(arr1, x)
    lst.append(result)

for x in lst:
    print(x)