
"""P017 - Count partitions with given difference"""
def count_partitions_with_diff(arr, diff):
    total=sum(arr)
    # solve for sum S such that S - (total-S) = diff => S = (total+diff)//2
    if (total+diff)%2!=0: return 0
    target=(total+diff)//2
    from collections import Counter
    dp=[0]*(target+1)
    dp[0]=1
    for num in arr:
        for s in range(target, num-1, -1):
            dp[s]+=dp[s-num]
    return dp[target]

if __name__=="__main__":
    assert count_partitions_with_diff([1,1,2,3],1)==3
    print("P017 OK")
