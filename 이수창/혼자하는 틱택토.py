import itertools
def solution(board):
    answer = -1
    countO = 0
    countX = 0
    new_board= []
    for item in board:
        for char in item:
            new_board.append(char)
    def checkWhoWin(target) :       
        wins=[
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
        ]
        for win in wins :
            [a,b,c] = win
            if new_board[a] == target and new_board[b] == target and new_board[c] == target :
                return True
        return False
    
    for i in range(len(board)):
        countO += board[i].count("O")
        countX += board[i].count("X")
    checkOWin = checkWhoWin("O")
    checkXWin = checkWhoWin("X")
    if checkOWin and checkXWin :
        return 0
    if countO < countX :
        return 0
    if countO - countX > 1 :
        return 0
    if  checkOWin and countO != countX + 1:
        return 0
    if checkXWin and countO != countX:
        return 0
    
    return 1