from collections import deque
def solution(maps):
    r = len(maps)
    c = len(maps[0])
    arr = []
    for map in maps :
        a = list(map)
        arr.append(a)
    maps = arr
    answer = []
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    q = deque()
    def bfs () :
        s = 0
        while q:
            x,y = q.popleft()
            for direction in directions:
                dx = x + direction[0]
                dy = y + direction[1]
                if 0<=dx<r and 0<=dy<c and maps[dx][dy] != "X":
                    s += int(maps[dx][dy])
                    maps[dx][dy] = "X"
                    q.append((dx,dy))
        return s
    for i in range(r) :
        for j in range(c) :
            if maps[i][j] != "X":
                count = int(maps[i][j])
                maps[i][j] = "X"
                q.append((i,j))
                count += bfs()
                answer.append(count)
    answer.sort()
    if len(answer) == 0 : answer = [-1]
    return answer