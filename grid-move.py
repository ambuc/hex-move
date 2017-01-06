#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

board = [
 [0,1,1],
 [0,3,4],
 [0,0,2]
]

state = [
 [0,0,0],
 [0,0,0],
 [3,2,4]
]

def draw(board, state):
    def drawSquare(b,s,n):
        def make(c):
            if c == 1: return '\033[0;30m'
            if c == 2: return '\033[0;31m'
            if c == 3: return '\033[0;32m'
            if c == 4: return '\033[0;34m'
            else:          return '\033[0m'
        def glyph(s):
            return "▒▒" if s != 0 else "  "
        if n==0: return make(b) + "┌──┐"
        if n==1: return make(b) + "│" + make(s) + glyph(s) + make(b) + "│"
        if n==2: return make(b) + "└──┘"
    n = len(board)
    output = ""
    for i in range(n):
        for s in range(3):
            for j in range(n):
                output += drawSquare(board[i][j], state[i][j],s)
            output += "\n"
    return output+"\033[0m"

def over(board,state):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] > 1:
                if state[i][j] != board[i][j]:
                    return False
    return True

def crunch(board,state,move):
    n = len(board)
    if move == "w":
        for i in range(1,n):
            for j in range(n):
                if state[i][j] != 0 and state[i-1][j] == 0 and board[i-1][j] != 1:
                    state[i-1][j], state[i][j] = state[i][j], 0
    if move == "s":
        for i in reversed(range(n-1)):
            for j in range(n):
                if state[i][j] != 0 and state[i+1][j] == 0 and board[i+1][j] != 1:
                    state[i+1][j], state[i][j] = state[i][j], 0
    if move == "a":
        for i in range(n):
            for j in range(1,n):
                if state[i][j] != 0 and state[i][j-1] == 0 and board[i][j-1] != 1:
                    state[i][j-1], state[i][j] = state[i][j], 0
    if move == "d":
        for i in range(n):
            for j in reversed(range(n-1)):
                if state[i][j] != 0 and state[i][j+1] == 0 and board[i][j+1] != 1:
                    state[i][j+1], state[i][j] = state[i][j], 0
    return state

def play(board, state):
    print "use asdw to move"
    print draw(board, state)
    while not over(board,state):
        move = raw_input()
        state = crunch(board,state,move)
        print draw(board, state)
    print "WINNER"

play(board,state)
