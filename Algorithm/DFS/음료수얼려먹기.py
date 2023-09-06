# dfs 상하좌우 탐색
# visited는 필요없을듯. 0,1,기준이 있기때문

def dfs (x,y):

    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        dfs(x+1,y)
        dfs(x - 1, y)
        dfs(x , y+1)
        dfs(x , y-1)

        return True

    return False

n,m = map(int, input().split())
result = 0

graph = []
for _ in range(n):
    line = list(map(int, input()))
    graph.append(line)
print(graph)




for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1
print(result)

