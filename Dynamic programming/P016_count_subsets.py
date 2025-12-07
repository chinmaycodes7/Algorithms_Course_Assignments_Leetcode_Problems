
"""P016 - Count subsets with sum K"""
def count_subsets(arr, K):
    dp=[0]*(K+1)
    dp[0]=1
    for num in arr:
        for s in range(K, num-1, -1):
            dp[s] += dp[s-num]
    return dp[K]

if __name__=="__main__":
    assert count_subsets([1,2,2,3],3)==3
    print("P016 OK")
