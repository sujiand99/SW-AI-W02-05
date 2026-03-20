# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478


def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1
    
if __name__=='__main__':
    n = int(input('출력할 팩토리얼값을 입력하세요.:'))
    print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')