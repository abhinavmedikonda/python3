from collections import deque
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        dpth = 2
        deq = deque([beginWord, None])
        bckt = set(wordList)
        while len(deq) > 1:
            word = deq.popleft()
            if not word:
                dpth += 1
                deq.append(None)
                continue
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    temp = word[:i] + c + word[i+1:]
                    if temp != word and temp in bckt:
                        if temp == endWord:
                            return dpth
                        deq.append(temp)
                        bckt.remove(temp)
        return 0

if __name__ == '__main__':
    o = Solution()
    print(o.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(o.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
    print(o.ladderLength("a", "c", ["a","b","c"]))
    print(o.ladderLength("aba", "bbc", ["aaa","aab","aac","aca","acc","baa","bbc","bca","bcc","ccb"]))
