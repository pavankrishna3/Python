import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def print_maze(stdscr,maze,path=[]):
    blue=curses.color_pair(2)
    for i, row in enumerate(maze):
        for j , value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"x",curses.color_pair(1)) # red color
            else:
                stdscr.addstr(i,j*2,value,blue)

def find_start(maze):

    for i, row in enumerate(maze):
        for j , value in enumerate(row):
            if value == 'O':
                return i,j

def find_path(stdscr,maze):
    end = "X"

    start = find_start(maze)
    visited = set()


    q = queue.Queue()
    q.put((start,[start]))

    while  not q.empty():
        pos , path = q.get()
        row , col = pos

        stdscr.clear()
        print_maze(stdscr,maze,path)
        
        time.sleep(0.2) 
        stdscr.refresh()

        
        
        if maze[row][col] == end:
            return path
        
        neigbours = find_neigbhours(row,col)

        for  neighbour in neigbours :
            if neighbour in visited:
                continue

            r,c = neighbour

            if maze[r][c] == "#":
                continue

            new_path = path + [neighbour]
            visited.add(neighbour)
            q.put((neighbour, new_path))


def find_neigbhours(row , col):
    neigbhours =[]
    if row > 0:
        neigbhours.append((row-1,col)) #up
    if row < len(maze)-1 :
        neigbhours.append((row+1,col))#down
    if  col>0:
        neigbhours.append((row,col-1))#left
    if col <len(maze[0])-1: 
        neigbhours.append((row,col+1))#right

    return neigbhours


def  main(stdscr):
    curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_BLUE,curses.COLOR_BLACK)

    find_path(stdscr,maze)
    stdscr.getkey()

wrapper(main)
