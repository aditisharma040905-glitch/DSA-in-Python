from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]

if __name__ == "__main__":

    arr = NumArray([-2, 0, 3, -5, 2, -1])
    print("Range Sum [0,2]:", arr.sumRange(0, 2))  # Expected 1
    print("Range Sum [2,5]:", arr.sumRange(2, 5))  # Expected -1
    print("Range Sum [0,5]:", arr.sumRange(0, 5))  # Expected -3