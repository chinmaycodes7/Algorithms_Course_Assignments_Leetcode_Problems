"""P019 - Longest subarray with given sum k (positives)
Brute: O(n^2) check all subarrays.
Optimized: sliding window (since positives) O(n).
"""

def brute_force(nums,k):
    n=len(nums)
    best=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=nums[j]
            if s==k:
                best=max(best,j-i+1)
    return best

def optimized(nums,k):
    i=0; s=0; best=0
    for j in range(len(nums)):
        s+=nums[j]
        while i<=j and s>k:
            s-=nums[i]; i+=1
        if s==k:
            best=max(best,j-i+1)
    return best

if __name__=='__main__':
    print(brute_force([10,5,2,7,1,9],15), optimized([10,5,2,7,1,9],15))
    print(brute_force([-3,2,1],6), optimized([-3,2,1],6))
