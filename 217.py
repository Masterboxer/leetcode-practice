from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numHashSet = set(nums)

        return len(numHashSet) < len(nums)


solution = Solution()

print(solution.containsDuplicate([1, 2, 3, 1]))
