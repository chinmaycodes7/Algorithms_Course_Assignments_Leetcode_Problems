"""P020 - Longest subarray sum K (positives + negatives)
Brute: O(n^2)
Optimized: prefix sum hashmap O(n)
"""

def brute_force(nums,k):
    n=len(nums); best=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=nums[j]
            if s==k:
                best=max(best,j-i+1)
    return best

def optimized(nums,k):
    pref=0; mp={0:-1}; best=0
    for i,x in enumerate(nums):
        pref+=x
        want = pref - k
        if want in mp:
            best = max(best, i - mp[want])
        if pref not in mp:
            mp[pref]=i
    return best

if __name__=='__main__':
    print(brute_force([10,5,2,7,1,9],15), optimized([10,5,2,7,1,9],15))
    print(brute_force([-3,2,1],6), optimized([-3,2,1],6))
