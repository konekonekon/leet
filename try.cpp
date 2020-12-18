#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>


class Solution {
public:
	std::vector<std::string> findAndReplacePattern(std::vector<std::string> &words, std::string pattern) {
		int pLength = pattern.length();
		std::cout << "The size of pattern is " << pLength << ".\n";

		std::vector<std::string> output = {"test"};
		return output;
	}

//def _get_pattern_list(self, pattern: str) -> List[List[int]]:
//        o = defaultdict(list)
//        for i, p in enumerate(pattern):
//            o[p].append(i)
//        #print(f'Dict of {pattern}: {o.values()}')
//        return list(o.values())
//
//    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
//        p_length = len(pattern)
//        p_list = self._get_pattern_list(pattern)
//        return [word for word in [w for w in words if len(w) == p_length]
//                if self._get_pattern_list(word) == p_list]

};


int main() {
	Solution sol;
	std::vector<std::string> words = {"abc", "vvv", "evv"};
	std::string patt = "mee";
	std::vector<std::string> output = sol.findAndReplacePattern(words, patt);

	return 0;
}

