import os
import time
import random
N=int(input("Enter grid size"))
class Grid:
    start=[]
    goal=[]
    l=[1,2]
    choice=l[random.randint(0,1)]
    if choice==1:
        start=[0,random.randint(0,N-1)]
    else:
        start=[N-1,random.randint(0,N-1)]
    if choice==1:
        goal=[random.randint(0,N-1),0]
    else:
        goal=[random.randint(0,N-1),N-1]
    def __init__(self,myObstacles,myRewards):
        self.myObstacles=myObstacles
        self.myRewards=myRewards
    A=[['.' for x in range(N)] for y in range(N)]
    def showGrid(self):
        os.system('cls')
        for i in range(N):
            for j in range(N):
                if (i,j) in self.myObstacles:
                    self.A[i][j]='#'
                elif (i,j) in self.myRewards:
                    self.A[i][j]=random.randint(1,9)
                if [i,j]==self.start:
                    self.A[i][j]='O'
                elif [i,j]==self.goal:
                    self.A[i][j]='[]'

        return ('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.A]))

class Obstacle:
    sam=random.sample(range((N-1)*(N-1)),N**2//6)
    o=[(i%(N-1) + 1, i//(N-1) + 1) for i in sam]
    def retob(self):
        return self.o

class Reward:
    sam=random.sample(range((N-1)*(N-1)),N**2//6)
    r=[(i%(N-1) + 1, i//(N-1) + 1) for i in sam]
    def retre(self):
        return self.r

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Player:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def set_x_y(A):
        for i in A:
            if 'O' in i:
                x=A.index(i)
                y=i.index('O')
                P=[x,y]
                break
        return P
    #Energy=50
    def makeMove(self,s,M,a,b):
        s+='I'
        for u in s:
            if u=='R':
                i=s.index('R')+1
                t=''
                while not(s[i].isalpha()):
                    t+=s[i]
                    i+=1
                if b+int(t)>N:
                    for i in range(1,N-int(t)+1):
                        [a,b]=self.set_x_y(M)
                        M[a][b]='.'
                        if b+2>=N:
                            break
                        M[a][b+1]='O'
                        os.system('cls')
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in M]))
                        time.sleep(0.5)
                    [a,b]=self.set_x_y(M)
                    M[a][b]='.'
                    [a,b]=[a,0]
                    M[a][b]='O'
                    os.system("cls")
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in M]))
                    for i in range(1,int(t)-N+b+1):
                        [a,b]=self.set_x_y(M)
                        M[a][b]='.'
                        M[a][b+1]='O'
                        os.system('cls')
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in M]))
                        time.sleep(0.5)
                else:
                    for i in range(1,int(t)+1):
                        [a,b]=self.set_x_y(M)
                        M[a][b]='.'
                        M[a][b+1]='O'
                        os.system('cls')
                        print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in M]))
                        time.sleep(0.5)
            if u=='L':
                i=s.index('L')+1
                t=''
                while not(s[i].isalpha()):
                    t+=s[i]
                    i+=1
                for i in range(1,int(t)+1):
                    [a,b]=self.set_x_y(M)
                    M[a][b]='.'
                    M[a][b-1]='O'
                    os.system('cls')
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in M]))
                    time.sleep(0.5)
            if u=='U':
                i=s.index('U')+1
                t=''
                while not(s[i].isalpha()):
                    t+=s[i]
                    i+=1
                for i in range(1,int(t)+1):
                    [a,b]=self.set_x_y(M)
                    M[a][b]='.'
                    M[a-1][b]='O'
                    os.system('cls')
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in M]))
                    time.sleep(0.5)
            if u=='D':
                i=s.index('D')+1
                t=''
                while not(s[i].isalpha()):
                    t+=s[i]
                    i+=1
                for i in range(1,int(t)+1):
                    [a,b]=self.set_x_y(M)
                    M[a][b]='.'
                    M[a+1][b]='O'
                    os.system('cls')
                    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in M]))
                    time.sleep(0.5)

obst=Obstacle
rewd=Reward
obst_=Obstacle.retob(obst)
rewd_=Reward.retre(rewd)
G=Grid(obst_,rewd_)
A=G.showGrid()
print(A)
M=G.A
P=Player
z=P.set_x_y(G.A)
print('player= ',z)
a=1
while(a):
    s=input("Enter Move ")
    P.makeMove(P,s,M,z[0],z[1])
    a=int(input("More moves? (0 for exit/1 for continue)"))
