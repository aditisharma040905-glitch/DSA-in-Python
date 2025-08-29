class Solution:
    def longestSubarrayWithSumK(self, nums, k):
        left = 0
        current_sum = 0
        max_length = 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum > k and left <= right:
                current_sum -= nums[left]
                left += 1

            if current_sum == k:
                max_length = max(max_length, right - left + 1)

        return max_length
    
# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 7, 5]
    k = 12
    print("Length of Longest Subarray with Sum at Most K:", Solution().longestSubarrayWithSumK(nums, k)) # Output: 3