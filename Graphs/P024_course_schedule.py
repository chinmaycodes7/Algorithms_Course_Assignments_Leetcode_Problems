# Auto-generated solution for P024: course_schedule

from typing import List
from collections import deque

# Problem P024: Course Schedule I & II (detect cycle and ordering)
def bruteforce_can_finish(numCourses:int, prerequisites:List[List[int]])->bool:
    # detect cycle using DFS
    adj=[[] for _ in range(numCourses)]
    for u,v in prerequisites:
        adj[v].append(u)
    visited=[0]*numCourses
    def dfs(u):
        visited[u]=1
        for v in adj[u]:
            if visited[v]==1: return False
            if visited[v]==0 and not dfs(v): return False
        visited[u]=2
        return True
    for i in range(numCourses):
        if visited[i]==0 and not dfs(i):
            return False
    return True

def bruteforce_find_order(numCourses:int, prerequisites:List[List[int]])->List[int]:
    indeg=[0]*numCourses
    adj=[[] for _ in range(numCourses)]
    for u,v in prerequisites:
        adj[v].append(u); indeg[u]+=1
    q=deque([i for i in range(numCourses) if indeg[i]==0])
    res=[]
    while q:
        u=q.popleft()
        res.append(u)
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:
                q.append(v)
    if len(res)!=numCourses: return []
    return res

optimized_can_finish = bruteforce_can_finish
optimized_find_order = bruteforce_find_order

def _test():
    assert bruteforce_can_finish(4, [[1,0],[2,1],[3,2]])==True
    assert bruteforce_find_order(4, [[1,0],[2,1],[3,2]])!=[]

if __name__=="__main__":
    _test()
    print("P024 tests passed")
