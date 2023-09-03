from collections import deque

def in_range(x, y, n, m):
    return x>=0 and x<n and y>=0 and y<m

def can_go(x, y, varr, marr):
    n = len(varr)
    m = len(varr[0])
    
    if not in_range(x, y, n, m):
        return False
    if varr[x][y]:
        return False
    if marr[x][y] == "X":
        return False
    return True

q = deque()

def move(x, y, step, varr, sarr):
    q.append((x, y, step))
    varr[x][y] = True
    sarr[x][y] = step
    
def bfs(sx, sy, step, lx, ly, marr):    
    n, m = len(marr), len(marr[0])
    
    q.clear()

    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]
    
    steps = [
        [-1 for _ in range(m)]
        for _ in range(n)
    ]
    
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    
    move(sx, sy, step, visited, steps)
    
    while q:
        x, y, s = q.popleft()

        if (x, y) == (lx, ly):
            return s
            
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            
            if can_go(nx, ny, visited, marr):
                move(nx, ny, s+1, visited, steps)
                
    return -1
    
def find_spot(arr2d, spot):
    for i, row in enumerate(arr2d):
        for j, elem in enumerate(row):
            if elem == spot:
                return i, j
            
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    sx, sy = find_spot(maps, "S")
    lx, ly = find_spot(maps, "L")
    ex, ey = find_spot(maps, "E")
    
    step_to_l = bfs(sx, sy, 0, lx, ly, maps)

    if step_to_l == -1:
        return -1
    
    step_to_e = bfs(lx, ly, step_to_l, ex, ey, maps)
    
    return step_to_e
