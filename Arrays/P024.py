"""P024 - Rearrange by sign (preserve relative order)
Brute: repeatedly insert (O(n^2)). Optimized: collect positives and negatives and interleave O(n).
"""
def brute_force(nums):
    # simulate by repeatedly finding next opposite sign and rotate
    res = nums[:]
    n=len(res)
    i=1
    while i<n:
        if (res[i-1]>0 and res[i]>0) or (res[i-1]<0 and res[i]<0):
            j=i+1
            while j<n and (res[j]>0)==(res[i]>0):
                j+=1
            if j==n: break
            val=res.pop(j); res.insert(i,val)
        i+=1
    return res

def optimized(nums):
    pos=[x for x in nums if x>0]
    neg=[x for x in nums if x<0]
    res=[]
    for a,b in zip(pos,neg):
        res.append(a); res.append(b)
    res += pos[len(neg):] + neg[len(pos):]
    return res

if __name__=='__main__':
    print(brute_force([2,4,5,-1,-3,-4]), optimized([2,4,5,-1,-3,-4]))
    print(brute_force([1,-1,-3,-4,2,3]), optimized([1,-1,-3,-4,2,3]))
