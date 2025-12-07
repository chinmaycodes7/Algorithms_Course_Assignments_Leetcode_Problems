"""P021 - Two Sum
Brute: O(n^2). Optimized: hashmap O(n).
Returns indices in increasing order.
"""
def brute_force(nums,target):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j]==target:
                return [i,j]
    return []

def optimized(nums,target):
    mp={}
    for i,x in enumerate(nums):
        need = target - x
        if need in mp:
            a=mp[need]; b=i
            return [a,b] if a<b else [b,a]
        mp[x]=i
    return []

if __name__=='__main__':
    print(brute_force([1,6,2,10,3],7), optimized([1,6,2,10,3],7))
    print(brute_force([1,3,5,-7,6,-3],0), optimized([1,3,5,-7,6,-3],0))
