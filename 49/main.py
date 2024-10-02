from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedHashMap = {}  # sorted : strings

        for s in strs:
            sorted_string = tuple(sorted(s))

            if sorted_string not in sortedHashMap:
                sortedHashMap[sorted_string] = [s]
            else:
                sortedHashMap[sorted_string].append(s)


        # This return method is faster by 10ms but returns a linting error in python3
        # but the code still runs.
        # return sortedHashMap.values()

        # Shows no linting error but is slower by 10ms
        return list(sortedHashMap.values()) 


solution = Solution()
result = solution.groupAnagrams(["eaten", "tea", "tane", "ate", "nat", "bat"])
print(result)
