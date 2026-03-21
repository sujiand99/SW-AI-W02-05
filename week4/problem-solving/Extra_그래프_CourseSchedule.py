# 그래프 - Course Schedule
# 문제 링크: https://leetcode.com/problems/course-schedule/?envType=study-plan-v2&envId=top-interview-150

from collections import deque

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque()
    queue.append(start_v)
    
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited


# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")