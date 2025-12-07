# Auto-generated solution for P018: word_ladder_i

from collections import deque
from typing import List, Set

# Problem P018: Word Ladder I
# bruteforce: BFS over all possible single-letter transformations generating characters 'a'..'z' (standard BFS)
def bruteforce_word_ladder(beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordset = set(wordList)
    if endWord not in wordset:
        return 0
    q = deque([(beginWord,1)])
    visited = {beginWord}
    while q:
        word,steps = q.popleft()
        if word == endWord:
            return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c==word[i]: continue
                nxt = word[:i]+c+word[i+1:]
                if nxt in wordset and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt,steps+1))
    return 0

# optimized: bidirectional BFS
def optimized_word_ladder(beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordset = set(wordList)
    if endWord not in wordset:
        return 0
    begin=set([beginWord]); end=set([endWord]); visited=set([beginWord,endWord]); step=1
    while begin and end:
        if len(begin) > len(end):
            begin, end = end, begin
        nxt=set()
        for word in begin:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c==word[i]: continue
                    new = word[:i]+c+word[i+1:]
                    if new in end:
                        return step+1
                    if new in wordset and new not in visited:
                        visited.add(new)
                        nxt.add(new)
        begin = nxt
        step += 1
    return 0

# simple tests
def _test():
    assert bruteforce_word_ladder("der","dfs",["des","der","dfr","dgt","dfs"]) == 3
    assert optimized_word_ladder("gedk","geek",["geek","gefk"]) == 2

if __name__=="__main__":
    _test()
    print("P018 tests passed")
