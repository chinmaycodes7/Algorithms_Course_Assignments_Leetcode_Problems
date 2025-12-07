# Auto-generated solution for P032: min_multiplications_mod

from collections import deque
from typing import List

# Problem P032: Minimum Multiplications to Reach End
def bruteforce_min_multiplications(arr:List[int], start:int, end:int)->int:
    MOD=100000
    dist=[-1]*MOD
    q=deque()
    q.append(start%MOD)
    dist[start%MOD]=0
    while q:
        cur=q.popleft()
        if cur==end: return dist[cur]
        for a in arr:
            nxt=(cur*a)%MOD
            if dist[nxt]==-1:
                dist[nxt]=dist[cur]+1
                q.append(nxt)
    return -1

optimized_min_multiplications = bruteforce_min_multiplications

def _test():
    assert bruteforce_min_multiplications([2,5,7],3,30)==2
    assert bruteforce_min_multiplications([3,4,65],7,66175)==4

if __name__=="__main__":
    _test()
    print("P032 tests passed")
