"""P027 - Rotate matrix 90 degrees clockwise
Brute: build a new rotated matrix. Optimized: transpose + reverse rows in-place.
"""
def brute_force(mat):
    n=len(mat)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n-1-i]=mat[i][j]
    return res

def optimized(mat):
    n=len(mat)
    a = [row[:] for row in mat]
    for i in range(n):
        for j in range(i,n):
            a[i][j],a[j][i]=a[j][i],a[i][j]
    for i in range(n):
        a[i].reverse()
    return a

if __name__=='__main__':
    m=[[1,2,3],[4,5,6],[7,8,9]]
    print(brute_force(m))
    print(optimized(m))
