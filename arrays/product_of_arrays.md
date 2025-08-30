# Day 6: Product of Array Except Self (leetcode 238)

## Problem Statement
Given an integer array `nums`,return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

We must solve it **without division** and in **O(n)** time.

---

# Exmaple
**Input:**
nums=[1,2,3,4]

**output**
[24,12,8,6]

---

## Approach
1. Compute prefix produxt for each index.
2. Compute suffix product in reverse order.
3. Multiply prefix and suffix values to get the result.

---

## Complexity
- Time Complexity: **O(n)**
- Sapce Complexity: **O(1)**
