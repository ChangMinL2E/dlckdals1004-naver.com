# 캐릭터의 좌표

'''
keyinput	board	result
["left", "right", "up", "right", "right"]	[11, 11]	[2, 1]
["down", "down", "down", "down", "down"]	[7, 9]	[0, -4]
'''

def solution(keyinput, board):
    x,y = board[0]//2, board[1]//2
    row, col = 0,0
    lst = ['up','down','right','left']
    
    for key in keyinput:
        if key == lst[0] and col < y:
            col += 1
        elif key == lst[1] and col > -y:
            col -= 1
        elif key == lst[2] and row < x:
            row += 1
        elif key == lst[3] and row > -x:
            row -= 1
    answer = [row,col]
    return answer