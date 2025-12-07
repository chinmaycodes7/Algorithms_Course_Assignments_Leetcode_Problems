"""P031 - Largest subarray with sum 0
Brute: O(n^2). Optimized: prefix sum hashmap.
"""
def brute_force(arr):
    n=len(arr); best=0
    for i in range(n):
        s=0
        for j in range(i,n):
            s+=arr[j]
            if s==0: best=max(best,j-i+1)
    return best

def optimized(arr):
    pref=0; mp={0:-1}; best=0
    for i,x in enumerate(arr):
        pref+=x
        if pref in mp:
            best=max(best, i-mp[pref])
        else:
            mp[pref]=i
    return best

if __name__=='__main__':
    print(brute_force([15,-2,2,-8,1,7,10,23]), optimized([15,-2,2,-8,1,7,10,23]))
    print(brute_force([2,10,4]), optimized([2,10,4]))
