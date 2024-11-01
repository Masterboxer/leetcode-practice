from typing import List


def bubble_sort(nums: List[int]):
    for n in range(len(nums) - 1, 0, -1):
        for i in range(n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


arr = [39, 12, 18, 85, 72, 10, 2, 18]

print(bubble_sort(arr))
