"""P025 - Next Permutation
Brute: generate permutations and pick next (works for small n). Optimized: standard algorithm in-place.
"""
import itertools

def brute_force(nums):
    perms = sorted(set(tuple(p) for p in itertools.permutations(nums)))
    t = tuple(nums)
    idx = perms.index(t)
    if idx+1 < len(perms):
        return list(perms[idx+1])
    return list(perms[0])

def optimized(nums):
    a = nums[:]
    n=len(a)
    i = n-2
    while i>=0 and a[i]>=a[i+1]:
        i-=1
    if i>=0:
        j=n-1
        while a[j]<=a[i]:
            j-=1
        a[i],a[j]=a[j],a[i]
    a[i+1:]=reversed(a[i+1:])
    return a

if __name__=='__main__':
    print(brute_force([1,2,3]), optimized([1,2,3]))
    print(brute_force([3,2,1]), optimized([3,2,1]))
