from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequentValuesHashmap = {}  # val : no. of times
        for n in nums:

            if n in frequentValuesHashmap:
                frequentValuesHashmap[n] = frequentValuesHashmap[n] + 1
            else:
                frequentValuesHashmap[n] = 1

        # print(frequentValuesHashmap)
        result: List[int] = []
        for h in frequentValuesHashmap:
            if frequentValuesHashmap[h] >= k:
                result.append(h)
                # print(h)
        return result


solution = Solution()
result = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(result)
