from collections import deque
def solution(maps):
   
    directions = [[1,0],[0,1],[-1,0],[0,-1]]
    def findLever ():
        q = deque()
        q.append(s)
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        while q :
            x,y,c = q.popleft()
            if maps[x][y] == "L":
                return c
            for direction in directions:
                dx = x + direction[0]
                dy = y + direction[1]
                if  0<=dx<len(maps) and 0<=dy<len(maps[0]) and not visited[dx][dy] and maps[dx][dy] != "X":
                    visited[dx][dy] = True
                    q.append((dx,dy,c+1))
        return -1
    def findExit ():
        q = deque()
        q.append(l)
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        while q :
            x,y,c = q.popleft()
            if maps[x][y] == "E":
                return c
            for direction in directions:
                dx = x + direction[0]
                dy = y + direction[1]
                if 0<=dx<len(maps) and 0<=dy<len(maps[0]) and maps[dx][dy] != "X" and not visited[dx][dy] :
                    visited[dx][dy] = True
                    q.append((dx,dy,c+1))
        return -1
    count = 0
    for i in range(len(maps)) :
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                s = (i,j,0)
            if maps[i][j] == "L":
                l = (i,j,0)
    countLever = findLever()
    if countLever == -1 :  return -1
    countExit = findExit()
    if countExit == -1 : return -1
    return countLever + countExit

    #visited를 큐에 넣기 전에 하는 것이 빠르다