# Auto-generated solution for P027: alien_dictionary

from typing import List
from collections import defaultdict, deque

# Problem P027: Alien Dictionary
def bruteforce_alien_dictionary(dict_words:List[str], K:int)->List[str]:
    adj=defaultdict(set); indeg={c:0 for c in ''.join(dict_words)}
    for i in range(len(dict_words)-1):
        w1,w2=dict_words[i],dict_words[i+1]
        minlen=min(len(w1),len(w2))
        for j in range(minlen):
            if w1[j]!=w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                break
    for u in adj:
        for v in adj[u]:
            indeg[v]+=1
    q=deque([c for c in indeg if indeg[c]==0])
    order=[]
    while q:
        c=q.popleft()
        order.append(c)
        for v in adj.get(c,[]):
            indeg[v]-=1
            if indeg[v]==0:
                q.append(v)
    return order

optimized_alien_dictionary = bruteforce_alien_dictionary

def _test():
    assert ''.join(bruteforce_alien_dictionary(["baa","abcd","abca","cab","cad"],4)) in ("bdac","bdca")

if __name__=="__main__":
    _test()
    print("P027 tests passed")
