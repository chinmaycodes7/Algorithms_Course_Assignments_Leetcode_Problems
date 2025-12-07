"""P037 - Count Inversions
Brute: O(n^2). Optimized: merge sort counting inversions O(n log n).
"""
def brute_force(nums):
    n=len(nums); cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]>nums[j]: cnt+=1
    return cnt

def optimized(nums):
    def merge_count(a):
        n=len(a)
        if n<=1: return a,0
        mid=n//2
        left,cl = merge_count(a[:mid])
        right,cr = merge_count(a[mid:])
        merged=[]; i=j=0; inv=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                merged.append(left[i]); i+=1
            else:
                merged.append(right[j]); j+=1
                inv += len(left)-i
        merged += left[i:]+right[j:]
        return merged, inv+cl+cr
    _, cnt = merge_count(list(nums))
    return cnt

if __name__=='__main__':
    print(brute_force([2,3,7,1,3,5]), optimized([2,3,7,1,3,5]))
    print(brute_force([-10,-5,6,11,15,17]), optimized([-10,-5,6,11,15,17]))
