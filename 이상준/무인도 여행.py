from collections import deque

def in_range(x, y, n, m):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x, y, varr, marr):
    n, m = len(varr), len(varr[0])
    
    if not in_range(x, y, n, m):
        return False
    if varr[x][y]:
        return False
    if marr[x][y] == "X":
        return False
    return True

q = deque()

def move(x, y, varr):
    q.append((x, y))
    varr[x][y] = True

def bfs(sx, sy, varr, marr):
    sum_val = int(marr[sx][sy])
    n, m = len(marr), len(marr[0])
    
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    
    move(sx, sy, varr)
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            
            if can_go(nx, ny, varr, marr):
                move(nx, ny, varr)
                sum_val += int(marr[nx][ny])
    
    return sum_val

def solution(maps):    
    answer = []
    
    n, m = len(maps), len(maps[0])
        
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    
    for i in range(n):
        for j in range(m):
            if can_go(i, j, visited, maps):
                answer.append(bfs(i, j, visited, maps))
                
    answer.sort()
    
    if answer:
        return answer
    else:
        return [-1]
