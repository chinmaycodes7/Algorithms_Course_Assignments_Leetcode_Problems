# Auto-generated solution for P019: word_ladder_ii

from collections import defaultdict, deque
from typing import List

# Problem P019: Word Ladder II
# bruteforce: BFS to compute distances then DFS to enumerate - naive but standard
def bruteforce_word_ladder_ii(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    wordset = set(wordList)
    if endWord not in wordset:
        return []
    # BFS to build graph of shortest paths
    layer = {beginWord: [[beginWord]]}
    while layer:
        newlayer = defaultdict(list)
        for word,paths in layer.items():
            if word == endWord:
                return paths
        for word,paths in layer.items():
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c==word[i]: continue
                    nxt = word[:i]+c+word[i+1:]
                    if nxt in wordset:
                        for p in paths:
                            newlayer[nxt].append(p+[nxt])
        wordset -= set(newlayer.keys())
        layer = newlayer
    return []

# optimized: same approach which is the common optimal method
optimized_word_ladder_ii = bruteforce_word_ladder_ii

def _test():
    res = bruteforce_word_ladder_ii("der","dfs",["des","der","dfr","dgt","dfs"])
    assert sorted(res) == sorted([["der","dfr","dfs"],["der","des","dfs"]])
    res2 = optimized_word_ladder_ii("gedk","geek",["geek","gefk"])
    assert res2 == [["gedk","geek"]]

if __name__=="__main__":
    _test()
    print("P019 tests passed")
