"""P030 - 3Sum: return unique triplets summing to zero
Brute: triple loops with dedup. Optimized: sort + two pointers.
"""
def brute_force(nums):
    n=len(nums); res=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    res.add(tuple(sorted((nums[i],nums[j],nums[k]))))
    return [list(t) for t in sorted(res)]

def optimized(nums):
    nums=sorted(nums); n=len(nums); res=[]
    for i in range(n):
        if i>0 and nums[i]==nums[i-1]: continue
        l=i+1; r=n-1
        while l<r:
            s=nums[i]+nums[l]+nums[r]
            if s==0:
                res.append([nums[i],nums[l],nums[r]])
                l+=1; r-=1
                while l<r and nums[l]==nums[l-1]: l+=1
                while l<r and nums[r]==nums[r+1]: r-=1
            elif s<0: l+=1
            else: r-=1
    return res

if __name__=='__main__':
    print(brute_force([2,-2,0,3,-3,5]), optimized([2,-2,0,3,-3,5]))
    print(brute_force([2,-1,-1,3,-1]), optimized([2,-1,-1,3,-1]))
