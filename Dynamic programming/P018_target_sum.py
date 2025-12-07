
"""P018 - Target Sum - count ways to reach target using +/- on elements"""
def find_target_sum_ways(arr, target):
    total=sum(arr)
    # convert to subset count: (total + target) must be even
    if abs(target) > total: return 0
    if (total + target) % 2 != 0: return 0
    s = (total + target)//2
    dp=[0]*(s+1)
    dp[0]=1
    for num in arr:
        for i in range(s, num-1, -1):
            dp[i]+=dp[i-num]
    return dp[s]

if __name__=="__main__":
    assert find_target_sum_ways([1,2,3,1],3)==2
    print("P018 OK")
