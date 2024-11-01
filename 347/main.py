from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        bucketSortingArray = [0] * (len(nums) + 1)
        finalAnswer = []

        for num, freq in counter.items():
            if bucketSortingArray[freq] == 0:
                bucketSortingArray[freq] = [num]
            else:
                bucketSortingArray[freq].append(num)

        for i in range(len(nums), -1, -1):
            if bucketSortingArray[i] != 0:
                if len(finalAnswer) != k:
                    finalAnswer.extend(bucketSortingArray[i])

        return finalAnswer


solution = Solution()
result = solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(result)
