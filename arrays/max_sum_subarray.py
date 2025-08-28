# Maximum Sum Subarray of Size K

class Solution:
    def maxSumSubarray(self, nums, k):
        # Step 1: Compute sum of first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum

    # Step 2: Slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum
    
# Example usage
if __name__ == "__main__":
    nums=[2,1,5,1,3,2]
    k=3
    print("Maximum Sum Subarray:", Solution().maxSumSubarray(nums,k)) # Output: 9

