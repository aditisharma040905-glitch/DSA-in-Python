def subarraySum(nums, k):
    prefix_sum = 0
    count = 0
    prefix_map = {0: 1}

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    return count

print("Subarray Sum Count [1,1,1], k=2:", subarraySum([1,1,1], 2))  # Expected 2
print("Subarray Sum Count [1,2,3], k=3:", subarraySum([1,2,3], 3))  # Expected 2