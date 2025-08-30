class solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        ans=[1]*n
        prefix=1
        for i in range(n):
            ans[i]=prefix
            prefix*=nums[i]

        suffix=1
        for i in range(n-1,-1,-1):
            ans[i]*=suffix
            suffix*=nums[i]
        return ans

# Example usage
if __name__ == "__main__":
    nums=[1,2,3,4]
    print("Product of Array Except Self:", solution().productExceptSelf(nums)) # Output: [24, 12, 8,6]