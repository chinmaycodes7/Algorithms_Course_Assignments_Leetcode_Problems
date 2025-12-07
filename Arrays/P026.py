"""P026 - Set Matrix Zeroes
Brute: use extra matrix to mark zeros then copy. Optimized: use first row/col as markers.
"""
import copy
def brute_force(mat):
    m=len(mat); n=len(mat[0]) if m else 0
    res = [row[:] for row in mat]
    rows=set(); cols=set()
    for i in range(m):
        for j in range(n):
            if mat[i][j]==0:
                rows.add(i); cols.add(j)
    for i in rows:
        for j in range(n): res[i][j]=0
    for j in cols:
        for i in range(m): res[i][j]=0
    return res

def optimized(mat):
    if not mat: return mat
    m=len(mat); n=len(mat[0])
    row0_zero = any(x==0 for x in mat[0])
    col0_zero = any(mat[i][0]==0 for i in range(m))
    for i in range(1,m):
        for j in range(1,n):
            if mat[i][j]==0:
                mat[i][0]=0; mat[0][j]=0
    for i in range(1,m):
        if mat[i][0]==0:
            for j in range(1,n): mat[i][j]=0
    for j in range(1,n):
        if mat[0][j]==0:
            for i in range(1,m): mat[i][j]=0
    if row0_zero:
        for j in range(n): mat[0][j]=0
    if col0_zero:
        for i in range(m): mat[i][0]=0
    return mat

if __name__=='__main__':
    m=[[1,1,1],[1,0,1],[1,1,1]]
    print(brute_force(m))
    print(optimized([row[:] for row in m]))
