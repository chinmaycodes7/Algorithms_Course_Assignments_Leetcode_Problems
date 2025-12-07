"""P022 - Sort an array of 0s,1s,2s
Brute: sort (creates new array). Optimized: Dutch National Flag in-place.
"""
def brute_force(nums):
    return sorted(nums)

def optimized(nums):
    a=nums[:]  # operate in-place on copy to keep function pure
    low=0; mid=0; high=len(a)-1
    while mid<=high:
        if a[mid]==0:
            a[low],a[mid]=a[mid],a[low]; low+=1; mid+=1
        elif a[mid]==1:
            mid+=1
        else:
            a[mid],a[high]=a[high],a[mid]; high-=1
    return a

if __name__=='__main__':
    print(brute_force([1,0,2,1,0]), optimized([1,0,2,1,0]))
    print(brute_force([0,0,1,1,1]), optimized([0,0,1,1,1]))
