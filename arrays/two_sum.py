# Day 1: Two Sum Problem

# Function to solve the problem
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}  # dictionary to store number:index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i

# Example run
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    obj = Solution()
    print("Result:", obj.twoSum(nums, target))  # Output: [0,1]
