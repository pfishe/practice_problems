# Word Search
#
# Problem: Given a 2D board of letters, determine if a given word can be
#          found on the board traversing horizontally or vertically.
#          Letters can only be used once.
#
# Example: [A B T]   ABT, ABLB, TBLF return true
#          [F L B]   ABA, AA, XYZ, TL return false
#
# Author: Drew Fisher
# Date: 7/6/18

import copy

def search_helper(board, word, i, j):
    #found word
    if len(word) == 0:
        return True
    #invalid step off board
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
        return False
    #invalid step to visited or wrong letter
    if board[i][j] != word[0]:
        return False
    #mark visited
    board[i][j] = ' '
    #steps
    exists = search_helper(board, word[1:],i+1,j) or search_helper(board, word[1:],i,j+1)\
        or search_helper(board, word[1:],i-1,j) or search_helper(board, word[1:],i,j-1)
    return exists

def search(board, word):
    starts = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                #refresh board for each search
                board_copy = copy.deepcopy(board)
                if search_helper(board_copy, word, i, j):
                    return True
    return False

board = [['A','A','A','A'],['A','B','B','A'],['A','A','A','A']]
word1 = 'ABC'     #false
word2 = 'AAAAAB'  #true
word3 = 'ABAB'    #false
word4 = 'ABAAAB'  #false
word5 = 'ABAAAAB' #true
print(search(board,word1))
print(search(board,word2))
print(search(board,word3))
print(search(board,word4))
print(search(board,word5))
