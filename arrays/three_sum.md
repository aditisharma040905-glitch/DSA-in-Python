# Day 2 - Three sum

## Problem 
Given an integer array `nums` return all the unique triplets `[nums[i],nums[j],nums[k]]` such that:
 -`i !-j` ,`i != k`, `j != k`
 - `nums[i]+nums[j]+nums[k]==0`

The solution set must not contain duplicate triplets.

## Example
**Input**
nums=[-1,0,1,2,-1,-4]

**Output**
[[-1,-1,2],[-1,0,1]]

## Approach
 1. **Sorting:** First,sort the array to make duplicate handling easier.
 2. **Fixed pointer +Two pointer:**
    - Iterate through each number as the fixed element.
    - Use two pointers (left,right) to find the pairs that sum with the fixed number to 0.
 3. **Skip duplicates:**
    - If the fixed number is the same as the previous, skip it.
    - While moving left and right ,skip duplicate numbers as well.

---

## Complexity
- **Time Complexity:** `O(n^2)` (Since for each element we use two pinter search).
- **Sapce Complexity:** `o(1)` (excluding output lsit).

---
