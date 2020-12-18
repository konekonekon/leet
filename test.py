from collections import defaultdict
from typing import List

class Solution:
    def _get_pattern_list(self, pattern: str) -> List[List[int]]:
        o = defaultdict(list)
        for i, p in enumerate(pattern):
            o[p].append(i)
        #print(f'Dict of {pattern}: {o.values()}')
        return o.values()

    def _match_list_of_list(self, l1: List, l2: List) -> bool:
        for i, item in enumerate(l1):
            if sorted(item) != sorted(l2[i]):
                return False
        return True

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p_list = sorted(self._get_pattern_list(pattern))
        return [word for word in words
                if self._match_list_of_list(sorted(self._get_pattern_list(word)), p_list)]


if __name__ == "__main__":
    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = 'abb'
    print(Solution().findAndReplacePattern(words, pattern))
