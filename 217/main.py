from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevSet = set()
        for n in nums:
            if n in prevSet:
                return True
            else:
                prevSet.add(n)
        return False


solution = Solution()

nums = [6, 3, 7, 4, 1, 7]
result = solution.containsDuplicate(nums)
print(result)
