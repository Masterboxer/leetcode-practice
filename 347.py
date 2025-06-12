from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucketSortedByFrequencyArray = [
            [] for _ in range(len(nums) + 1)
        ]  # frequency is the index of the array
        frequencyHashmap = {}  # value : frequency
        outputArray = []

        for num in nums:
            if num in frequencyHashmap:
                frequencyHashmap[num] = frequencyHashmap[num] + 1
            else:
                frequencyHashmap[num] = 1

        for element in frequencyHashmap:
            bucketSortedByFrequencyArray[frequencyHashmap[element]].append(element)

        for frequency in range(len(bucketSortedByFrequencyArray) - 1, 0, -1):
            for val in bucketSortedByFrequencyArray[frequency]:
                outputArray.append(val)
                if len(outputArray) == k:
                    return outputArray


solution = Solution()
print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
