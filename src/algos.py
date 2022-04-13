from constants import *

def algo(arr,source_x,source_y,dest_x,dest_y):
        directions = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        visited = [[False for i in range(ROWS_V)] for j in range(COLS_V)]
        path = [[None for i in range(ROWS_V)] for j in range(COLS_V)]
        q = []
        q.append([source_x,source_y])
        path[source_x][source_y] = [[source_x,source_y]]
        while(len(q)>0):
            p = q[0]
            q.pop(0)
            visited[p[0]][p[1]] = True
            for i in range(len(directions)):
                x = p[0] + directions[i][0]
                y = p[1] + directions[i][1]
                if(x>=0 and x<ROWS_V and y>=0 and y<COLS_V and arr[x][y]!=-1 and visited[x][y]==False):
                    q.append([x,y])
                    visited[x][y] = True
                    path[x][y] = path[p[0]][p[1]] + [[x,y]]
        if(visited[dest_x][dest_y]):
            return path[dest_x][dest_y]
        else:
            return False

