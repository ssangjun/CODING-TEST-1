def counter(arr2d):
    o_cnt, x_cnt = 0, 0
    for row in arr2d:
        o_cnt += row.count("O")
        x_cnt += row.count("X")
    return o_cnt, x_cnt

def in_range(x, y):
    return x>=0 and x<3 and y>=0 and y<3

def is_win(arr2d, elem):
    dxs = [-1, -1, 0, 1, 1,  1,  0, -1]
    dys = [ 0,  1, 1, 1, 0, -1, -1, -1]
    
    for dx, dy in zip(dxs, dys):
        for i in range(3):
            for j in range(3):
                if arr2d[i][j] == elem:
                    nx, ny = i+dx, j+dy
                    
                    if in_range(nx, ny) and arr2d[nx][ny]  == elem:
                        mx, my = nx+dx, ny+dy
                        
                        if in_range(mx, my) and arr2d[mx][my]  == elem:
                            return True
                        
    return False
            
def solution(board):
    answer = -1
    o_cnt, x_cnt = counter(board)
    
    if o_cnt < x_cnt:
        return 0
    
    if o_cnt > x_cnt + 1:
        return 0
    
    if o_cnt == x_cnt and is_win(board, "O"):
        return 0
    
    if o_cnt == x_cnt + 1 and is_win(board, "X"):
        return 0
    
    return 1
    
