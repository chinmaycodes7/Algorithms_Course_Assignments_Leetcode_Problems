
"""P005 - House Robber II (circular houses)"""
def rob_linear(nums):
    prev, curr = 0,0
    for x in nums:
        prev, curr = curr, max(curr, prev+x)
    return curr

def top_down(nums):
    n=len(nums)
    if n==1: return nums[0]
    # try two ranges: [0..n-2], [1..n-1]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

def bottom_up(nums):
    return top_down(nums)  # linear reuse

def space_optimized(nums):
    return top_down(nums)

if __name__=="__main__":
    arr=[2,3,2]
    assert top_down(arr)==3
    assert bottom_up(arr)==3
    assert space_optimized(arr)==3
    print("P005 OK")
