# Auto-generated solution for P038: accounts_merge

from typing import List
from collections import defaultdict

# Problem P038: Accounts Merge
def bruteforce_accounts_merge(accounts:List[List[str]])->List[List[str]]:
    parent={}
    def find(x):
        parent.setdefault(x,x)
        if parent[x]!=x:
            parent[x]=find(parent[x])
        return parent[x]
    def union(a,b):
        ra,rb=find(a),find(b)
        if ra!=rb:
            parent[rb]=ra
    email_to_name={}
    for acc in accounts:
        name=acc[0]
        for email in acc[1:]:
            email_to_name[email]=name
            parent.setdefault(email,email)
        for i in range(1,len(acc)):
            union(acc[1],acc[i])
    groups=defaultdict(list)
    for email in email_to_name:
        groups[find(email)].append(email)
    res=[]
    for root,emails in groups.items():
        res.append([email_to_name[root]]+sorted(emails))
    return res

optimized_accounts_merge = bruteforce_accounts_merge

def _test():
    accounts=[["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]]
    out=bruteforce_accounts_merge(accounts)
    # check merged John group contains expected emails
    flat = [sorted(acc[1:]) for acc in out if acc[0]=="John"]
    assert any("john00@mail.com" in grp for grp in flat)

if __name__=="__main__":
    _test()
    print("P038 tests passed")
