"""P036 - Find repeating and missing number
Brute: counts. Optimized: use xor trick.
"""
from collections import Counter
def brute_force(nums):
    n=len(nums)
    cnt=Counter(nums)
    A = next(x for x,c in cnt.items() if c==2)
    B = next(x for x in range(1,n+1) if x not in cnt)
    return [A,B]

def optimized(nums):
    n=len(nums)
    x1 = 0
    for v in nums:
        x1 ^= v
    for i in range(1,n+1):
        x1 ^= i
    set_bit = x1 & -x1
    a=b=0
    for v in nums:
        if v & set_bit: a ^= v
        else: b ^= v
    for i in range(1,n+1):
        if i & set_bit: a ^= i
        else: b ^= i
    if nums.count(a)==2:
        return [a,b]
    else:
        return [b,a]

if __name__=='__main__':
    print(brute_force([3,5,4,1,1]), optimized([3,5,4,1,1]))
    print(brute_force([1,2,3,6,7,5,7]), optimized([1,2,3,6,7,5,7]))
