from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val : ind

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i
        return [0, 1]


solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)
