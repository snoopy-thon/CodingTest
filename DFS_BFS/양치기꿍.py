R, C = map(int, input().split())

graph = []
for i in range(R):
  graph.append(list(input()))


def dfs(x, y):
  global sheep, wolf
  if x <= -1 or x >= R or y <= -1 or y >= C:
    return
  if graph[x][y] == '.' or graph[x][y] == 'v' or graph[x] == 'k':
    graph[x][y] = '#'
    if graph[x][y] == 'v':
      wolf += 1
    elif graph[x][y] == 'k':
      sheep += 1
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False



sh_result = 0
wol_result = 0

for i in range(R):
  for j in range(C):
    if dfs(i, j) == True:
      if sheep > wolf:
        sh_result += sheep
        wol_result -= wolf
      else:
        sh_result -= sheep
        wol_result += wolf


print("sheep_result:%d wolf_result:%d" %(sh_result, wol_result))
    