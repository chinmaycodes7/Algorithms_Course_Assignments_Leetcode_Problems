"""P035 - Count subarrays with given XOR K
Brute: O(n^2) compute xor for each subarray. Optimized: prefix xor + hashmap.
"""
from collections import defaultdict
def brute_force(nums,k):
    n=len(nums); cnt=0
    for i in range(n):
        xr=0
        for j in range(i,n):
            xr ^= nums[j]
            if xr==k: cnt+=1
    return cnt

def optimized(nums,k):
    mp=defaultdict(int); mp[0]=1
    xr=0; cnt=0
    for x in nums:
        xr ^= x
        want = xr ^ k
        cnt += mp.get(want,0)
        mp[xr]+=1
    return cnt

if __name__=='__main__':
    print(brute_force([4,2,2,6,4],6), optimized([4,2,2,6,4],6))
    print(brute_force([5,6,7,8,9],5), optimized([5,6,7,8,9],5))
