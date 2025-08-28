# Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums, k):
        # Compute sum of first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Step 2: Slide the window
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]  # slide by removing first and adding new
            max_sum = max(max_sum, window_sum)

        # Step 3: Return maximum average
        return float(max_sum) / k
    
# Example usage
if __name__ == "__main__":
    nums=[1,12,-5,-6,50,3]
    k=4
    print("Maximum Average Subarray:", Solution().findMaxAverage(nums,k)) # Output: 12.75

