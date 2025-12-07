
"""P006 - Ninja Training (max points with 3 activities)"""
from functools import lru_cache
def top_down(points):
    n=len(points)
    @lru_cache(None)
    def dfs(day, last):
        if day==n: return 0
        best=0
        for act in range(3):
            if act==last: continue
            best=max(best, points[day][act] + dfs(day+1, act))
        return best
    return dfs(0, -1)

def bottom_up(points):
    n=len(points)
    dp=[[0]*4 for _ in range(n+1)]
    # last = 0,1,2,3 where 3 means no last restriction
    for day in range(n-1, -1, -1):
        for last in range(4):
            best=0
            for act in range(3):
                if act==last: continue
                best=max(best, points[day][act] + dp[day+1][act])
            dp[day][last]=best
    return dp[0][3]

def space_optimized(points):
    n=len(points)
    next_row=[0]*4
    for day in range(n-1, -1, -1):
        curr=[0]*4
        for last in range(4):
            best=0
            for act in range(3):
                if act==last: continue
                best=max(best, points[day][act]+ next_row[act])
            curr[last]=best
        next_row=curr
    return next_row[3]

if __name__=="__main__":
    pts=[[1,2,5],[3,1,1],[3,2,1]]
    assert top_down(pts)==9
    assert bottom_up(pts)==9
    assert space_optimized(pts)==9
    print("P006 OK")
