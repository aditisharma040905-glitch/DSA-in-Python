def pivotIndex(nums):
    total_sum = sum(nums)
    left_sum = 0
    for i, num in enumerate(nums):
        if left_sum == (total_sum - left_sum - num):
            return i
        left_sum += num
    return -1

print("Pivot Index of [1,7,3,6,5,6]:", pivotIndex([1,7,3,6,5,6]))  # Expected 3
print("Pivot Index of [1,2,3]:", pivotIndex([1,2,3]))              # Expected -1
