# Day  9 - Sliding Window (Fixed Size)

Today ,we explored **slinding window technique** for fixed_size windows.Sliding Window is useful when we need to process **contiguous subarrays** efficently.

## Problem 1: Maximum Average subarray I 

**Problem Statement:**
We have given an integer array `nums` consiting of `n` elements, and an integer `k`.
Find a contiguous subarray of length `k` that has the maximum average value , and return this value.

#### Example:
Input:  
nums = [1,12,-5,-6,50,3], k = 4
Output:  
12.75

# Explanation:  
The subarray `[12, -5, -6, 50]` has the maximum average `(12 - 5 - 6 + 50) / 4 = 51/4 = 12.75`.

---
## Approach 
- Calculate the sum of the first `k` elements.
- Slide the window forward one element at a time:
  - Add the new element, remove the old one.
- Keep track of the maximum sum found.
- Fianlly, divide by `k` to get the maximum average.

---
## Complexity
Time complexity: O(n)
Sapce Complexity: O(1)

---

## Problem 2: Maximum Sum Subarray of Size K

# Problem Statement
Given an array of integers `nums` and an integer `k`
, find the **maximum sum of any contiguous subarray of size `k`**.

## Example
Input:
nums=[2,1,5,1,3,2],k=3
Output:
9

# Explanation:
The subarray `[5,1,3]` has the maximum sum of `9`.

---
# Appraoch 
We us the **sliding window technique**:
1. Compute the sum of the first `k` elements.
2. Move the window one element at a time -> Subtract the element going out an add the new element coming in.
3. Keep updating the maximum sum.

---
# Complexity
Time complexity: O(n)'
Space Complexity:O(1)

---
Both problems are solved using the **fixed-size sliding window technique**.