# 2021/09/01
# DFS / BFS 알고리즘
# 5-9. BFS 예제 / BFS(= 너비 우선 탐색) : 가까운 노드부터 탐색하는 알고리즘
# BFS 구현에서는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석임.

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력(가장 먼저 넣은 원소)
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:  # 해당 노드가 방문되지 않았다면 방문.
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9
# 정의된 BFS 함수 호출
bfs(graph,1,visited)
