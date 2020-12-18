from collections import defaultdict
from typing import List

class Solution:
    # idea is to create a dict of list of each character in an input string and its position in the string. Then to get only the positions.
    # E.g. "mee" => {"m": [0], "e": [1,2]} => [[0], [1,2]]
    def _get_pattern_list(self, pattern: str) -> List[List[int]]:
        o = defaultdict(list)
        for i, p in enumerate(pattern):
            o[p].append(i)
        #print(f'Dict of {pattern}: {o.values()}')
        return list(o.values())

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        p_length = len(pattern)
        p_list = self._get_pattern_list(pattern)
        return [word for word in [w for w in words if len(w) == p_length]
                if self._get_pattern_list(word) == p_list]


if __name__ == "__main__":
    words = ["abc","deq","mee","aqq","dkd","ccc"]
    pattern = 'abb'
    print(Solution().findAndReplacePattern(words, pattern))
