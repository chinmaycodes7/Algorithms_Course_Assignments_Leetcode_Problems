"""P033 - Merge two sorted arrays without extra space
Brute: concatenate and sort (uses extra space). Optimized: merge from end into nums1 assuming nums1 has space.
"""
def brute_force(nums1, m, nums2, n):
    a = nums1[:m] + nums2[:n]
    return sorted(a)

def optimized(nums1, m, nums2, n):
    # nums1 has length m+n with trailing zeros
    i=m-1; j=n-1; k=m+n-1
    a=nums1[:]  # operate on copy to return
    while j>=0:
        if i>=0 and a[i]>nums2[j]:
            a[k]=a[i]; i-=1
        else:
            a[k]=nums2[j]; j-=1
        k-=1
    return a

if __name__=='__main__':
    print(brute_force([-5,-2,4,5],4,[-3,1,8],3))
    print(optimized([-5,-2,4,5,0,0,0],4,[-3,1,8],3))
