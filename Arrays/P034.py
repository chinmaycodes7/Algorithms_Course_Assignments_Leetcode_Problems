"""P034 - 4Sum
Brute: quadruple loops. Optimized: sort + two pointers nested for two outer loops.
"""
def brute_force(nums,target):
    n=len(nums); res=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if nums[i]+nums[j]+nums[k]+nums[l]==target:
                        res.add(tuple(sorted((nums[i],nums[j],nums[k],nums[l]))))
    return [list(t) for t in sorted(res)]

def optimized(nums,target):
    nums=sorted(nums); n=len(nums); res=[]
    for i in range(n):
        if i>0 and nums[i]==nums[i-1]: continue
        for j in range(i+1,n):
            if j>i+1 and nums[j]==nums[j-1]: continue
            left=j+1; right=n-1
            while left<right:
                s=nums[i]+nums[j]+nums[left]+nums[right]
                if s==target:
                    res.append([nums[i],nums[j],nums[left],nums[right]])
                    left+=1; right-=1
                    while left<right and nums[left]==nums[left-1]: left+=1
                    while left<right and nums[right]==nums[right+1]: right-=1
                elif s<target: left+=1
                else: right-=1
    return res

if __name__=='__main__':
    print(brute_force([1,-2,3,5,7,9],7), optimized([1,-2,3,5,7,9],7))
    print(brute_force([7,-7,1,2,14,3],9), optimized([7,-7,1,2,14,3],9))
