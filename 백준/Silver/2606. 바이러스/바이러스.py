import sys
input = sys.stdin.readline

def dfs(start):
  visited[start] = True
  for i in graph[start]:
    if not visited[i]:
      dfs(i)

com = int(input())
edge = int(input())
graph = [[] for _ in range(com+1)]
visited = [False] * (com+1)

for i in range(edge):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(1)
print(visited.count(True)-1)