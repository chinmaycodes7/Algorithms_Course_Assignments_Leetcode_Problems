"""P029 - Majority Element II (elements > n/3 times)
Brute: count frequencies. Optimized: Boyer-Moore majority generalized.
"""
from collections import Counter
def brute_force(nums):
    n=len(nums)
    cnt=Counter(nums)
    return [x for x,c in cnt.items() if c> n//3]

def optimized(nums):
    if not nums: return []
    a=b=None; ca=cb=0
    for x in nums:
        if a==x:
            ca+=1
        elif b==x:
            cb+=1
        elif ca==0:
            a=x; ca=1
        elif cb==0:
            b=x; cb=1
        else:
            ca-=1; cb-=1
    res=[]
    for cand in (a,b):
        if cand is None: continue
        if nums.count(cand)>len(nums)//3:
            if cand not in res: res.append(cand)
    return res

if __name__=='__main__':
    print(brute_force([1,2,1,1,3,2]), optimized([1,2,1,1,3,2]))
    print(brute_force([1,2,1,1,3,2,2]), optimized([1,2,1,1,3,2,2]))
