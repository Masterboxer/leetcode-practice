from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedAnagramHashmap = {}  # anagram : groupedAnagrams
        for s in strs:
            if "".join(sorted(s)) in groupedAnagramHashmap:
                groupedAnagramHashmap["".join(sorted(s))].append(s)
            else:
                groupedAnagramHashmap["".join(sorted(s))] = [s]
        return list(groupedAnagramHashmap.values())


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
count = [0] * 26
print(count)
