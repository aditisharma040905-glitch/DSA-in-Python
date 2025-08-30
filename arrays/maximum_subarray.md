# Day 4 -Maximum Subarray(kadanec's Algorithm)

**Problem:** [Leetcode 53 -Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)


### 🔹 Problem Statement
Given an integer array `nums`,find the contiguous subarray (containing at least  one number) which has the largest sum and return its sum.

---

### Approach (kadane's Algorithm)
-keep two variables:
 - `current_sum` -> maximum subarray sum ending at current index.
 -  `max_sum` -> maximum subarray sum found so far.
-At each step:
 - Either extend the current subarray(`current_sum +nums[i]`)
 -Update `max_sum` with the maximum found so far.

Time complexity: **O(n)**
Space complxity: **O(1)**

---
### Example
Input: `nums=[-2,1,-3,4,-1,2,1,-5,4]`
Output: `6`
Explanation:The subarray`[4,-1,2,1]` has the largest sum=6.


