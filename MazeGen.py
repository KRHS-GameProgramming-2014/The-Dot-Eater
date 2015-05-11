from random import randint
from os import system
from time import sleep

def grid(width, height):
    board=[]
    if width%2==0:
        width+=1
    else:
        width+=0
    if height%2==0:
        height+=1
    else:
        height+=0
    for row in range(height-2):
        myRow=[]
        for item in range(width):
            if row%2==1 and item%2==1:
                myRow+=[" "]
            else:
                myRow+=["#"]
        board+=[myRow]
    return board

def print_maze(maze):
    board=""
    for row in maze:
        myRow=""
        for item in row:
            myRow+=item
        board+=myRow+"\n"
    print board

def write_maze(fileName, maze):
    board=""
    for row in maze:
        myRow=""
        for item in row:
            myRow+=item
        board+=myRow+"\n"
    file=open(fileName, "w")
    file.write(board)
    file.close

def intact(board, x, y):
    if (board[x+1][y]=="#" and \
        board[x-1][y]=="#" and \
        board[x][y+1]=="#" and \
        board[x][y-1]=="#"):
        return True
    else:
        return False

def maze(width, height):
    board=grid(width, height)
    startx=2
    starty=2
    while startx%2==0:
        startx=randint(1, height-3)
    while starty%2==0:
        starty=randint(1, width-3)
    print startx, len(board), starty, len(board[0])
    board[startx][starty]="@"
    x=startx
    y=starty

    totalcells=(width/2)*(height/2)
    visitedcells=1
    cellstack=[]


    while visitedcells<totalcells:
        opts=[]
        if 0<x<len(board)-2:
            if intact(board,x+2,y):
                opts+=[[x+2,y]]
        if 2<x<len(board):
            if intact(board,x-2,y):
                opts+=[[x-2,y]]
        if 0<y<len(board[0])-2:
            if intact(board,x,y+2):
                opts+=[[x,y+2]]
        if 2<y<len(board[0]):
            if intact(board,x,y-2):
                opts+=[[x,y-2]]
        if len(opts):
            mycoor=opts[randint(0,len(opts)-1)]
            nx=mycoor[0]
            ny=mycoor[1]
            if nx!=x:
                board[(x+nx)/2][y]=" "
                board[x][y]=" "
                x=nx
                y=ny
                board[x][y]="@"
            elif ny!=y:
                board[x][(y+ny)/2]=" "
                board[x][y]=" "
                x=nx
                y=ny
                board[x][y]="@"
            visitedcells+=1
            cellstack+=[mycoor]
        else:
            if len(cellstack):
                mycoor=cellstack.pop()
                board[x][y]=" "
                x=mycoor[0]
                y=mycoor[1]
                board[x][y]="@"
            else:
                board[x][y]=" "
                return board



        #system("cls")
        #print_maze(board)
        #sleep(.005)
        print visitedcells, len(cellstack), totalcells

    return board

