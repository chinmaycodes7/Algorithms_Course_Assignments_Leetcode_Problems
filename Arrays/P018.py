"""P018 - Single Number
Brute force: count occurrences.
Optimized: XOR all numbers.
"""
from collections import Counter

def brute_force(nums):
    cnt = Counter(nums)
    for k,v in cnt.items():
        if v==1:
            return k
    return None

def optimized(nums):
    res = 0
    for x in nums:
        res ^= x
    return res

if __name__ == '__main__':
    tests = [[1,2,2,4,3,1,4],[5],[0,0,1]]
    for t in tests:
        print('nums=',t,'brute=',brute_force(t),'opt=',optimized(t))
