import collections
def tresure(island):
    if not island or len(island) == 0:
        return 0
    steps = 0
    queue = collections.deque()
    queue.append((0,0))
    visited = [[False for _ in range(len(island[0]))] for _ in range(len(island))]
    visited[0][0] = True
    dirs = [[1,0],[-1,0],[0,1],[0,-1]]
    while queue:
        for _ in range(len(queue)):
            x,y = queue.pop()
            if island[x][y] == 'X':
                return steps
            for dir in dirs:
                newX = x+dir[0]
                newY = y+dir[1]
                if newX >= 0 and newX < len(island) and newY >= 0 and newY < len(island[0]) and island[newX][newY] != 'D' and  not visited[newX][newY]:
                    queue.append((newX, newY))
                    visited[newX][newY] = True
        steps+=1
    return 0


island = [['O', 'O', 'O', 'O'],
			['D', 'O', 'D', 'O'],
			['O', 'O', 'O', 'O'],
			['X', 'D', 'D', 'O']]
print(tresure(island))