"""P028 - Print matrix in spiral order
Brute: simulate visited boolean. Optimized: use boundary indices.
"""
def brute_force(mat):
    if not mat: return []
    m=len(mat); n=len(mat[0])
    visited=[[False]*n for _ in range(m)]
    dirs=[(0,1),(1,0),(0,-1),(-1,0)]
    d=0; i=0;j=0; res=[]
    for _ in range(m*n):
        res.append(mat[i][j]); visited[i][j]=True
        ni=i+dirs[d][0]; nj=j+dirs[d][1]
        if 0<=ni<m and 0<=nj<n and not visited[ni][nj]:
            i,j=ni,nj
        else:
            d=(d+1)%4
            i+=dirs[d][0]; j+=dirs[d][1]
    return res

def optimized(mat):
    if not mat: return []
    top,bot, left, right = 0, len(mat)-1, 0, len(mat[0])-1
    res=[]
    while top<=bot and left<=right:
        for j in range(left,right+1): res.append(mat[top][j])
        top+=1
        for i in range(top,bot+1): res.append(mat[i][right])
        right-=1
        if top<=bot:
            for j in range(right,left-1,-1): res.append(mat[bot][j])
            bot-=1
        if left<=right:
            for i in range(bot,top-1,-1): res.append(mat[i][left])
            left+=1
    return res

if __name__=='__main__':
    print(brute_force([[1,2,3],[4,5,6],[7,8,9]]))
    print(optimized([[1,2,3,4],[5,6,7,8]]))
