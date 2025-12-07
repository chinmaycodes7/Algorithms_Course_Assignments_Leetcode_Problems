"""P032 - Merge Overlapping Intervals
Brute: compare all and merge repeatedly. Optimized: sort by start and merge once.
"""
def brute_force(intervals):
    intervals = [list(i) for i in intervals]
    changed=True
    while changed:
        changed=False
        n=len(intervals)
        i=0
        while i<n:
            j=i+1
            while j<n:
                a=intervals[i]; b=intervals[j]
                if not (a[1]<b[0] or b[1]<a[0]):
                    intervals[i]=[min(a[0],b[0]), max(a[1],b[1])]
                    intervals.pop(j); n-=1; changed=True
                else:
                    j+=1
            i+=1
    return intervals

def optimized(intervals):
    if not intervals: return []
    intervals=sorted(intervals,key=lambda x:x[0])
    res=[intervals[0][:]]
    for s,e in intervals[1:]:
        if s<=res[-1][1]:
            res[-1][1]=max(res[-1][1], e)
        else:
            res.append([s,e])
    return res

if __name__=='__main__':
    print(brute_force([[1,5],[3,6],[8,10],[15,18]]))
    print(optimized([[5,7],[1,3],[4,6],[8,10]]))
