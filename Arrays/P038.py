"""P038 - Reverse Pairs
Brute: O(n^2). Optimized: modified merge sort counting suitable pairs.
"""
def brute_force(nums):
    n=len(nums); cnt=0
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] > 2*nums[j]: cnt+=1
    return cnt

def optimized(nums):
    def sort_count(a):
        n=len(a)
        if n<=1: return a,0
        mid=n//2
        left,cl = sort_count(a[:mid])
        right,cr = sort_count(a[mid:])
        cnt=cl+cr
        j=0
        # count cross pairs
        for i in range(len(left)):
            while j<len(right) and left[i] > 2*right[j]:
                j+=1
            cnt += j
        # merge
        merged=[]; i=j2=0
        while i<len(left) and j2<len(right):
            if left[i]<=right[j2]:
                merged.append(left[i]); i+=1
            else:
                merged.append(right[j2]); j2+=1
        merged += left[i:]+right[j2:]
        return merged, cnt
    _, c = sort_count(list(nums))
    return c

if __name__=='__main__':
    print(brute_force([6,4,1,2,7]), optimized([6,4,1,2,7]))
    print(brute_force([5,4,4,3,3]), optimized([5,4,4,3,3]))
