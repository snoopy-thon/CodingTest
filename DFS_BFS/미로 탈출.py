from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
  graph.append(list(map(int, input())))

