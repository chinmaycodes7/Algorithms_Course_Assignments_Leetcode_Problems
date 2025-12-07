"""P023 - Kadane's Algorithm (Max subarray sum)
Brute: O(n^2) check all subarrays. Optimized: Kadane O(n).
"""
def brute_force(nums):
    n=len(nums)
    best=nums[0] if n else 0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=nums[j]; best=max(best,s)
    return best

def optimized(nums):
    best = nums[0]; cur=0
    for x in nums:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best

if __name__=='__main__':
    print(brute_force([2,3,5,-2,7,-4]), optimized([2,3,5,-2,7,-4]))
    print(brute_force([-2,-3,-7,-2,-10,-4]), optimized([-2,-3,-7,-2,-10,-4]))
