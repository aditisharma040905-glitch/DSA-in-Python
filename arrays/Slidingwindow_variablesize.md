# Day 10 -  Sliding Window (Variable size)

Today we cover **variable size sliding window problems**.
Unlike fixed-size, here the window **expands and shrinks dynamically** based on a condition.

---

# Problem: Longest Substring Without Repeating Characters

## Problem Statement
Given a string `s` ,find the length of the longest substring without repeating cahracters.

## Example
Input:
`s="abcabcbb"`
Output:
`3`
Explanation: The answer is "abs", with length 3.

## Approach
- Use two pointers(`left`,`right`) to represent a window.
- Expand`right` and include characters until a duplicate is found.
- When duplicate appears ,shrink from `left` until valid.
- Keep track of maximum length.

## Complexity
- Time Complexity -o(n)
- Space complexity-O(1)

---

## Problem 2: Longest Subarray with Sum <=K

### Problem Statment
Given an array of integers `nums` an an integer `k`,
find the length of the lowest subarray such that the **sum<=k**.

## Example
Input:
`nums = [2,3,1,2,4,3],k=7`
Output: 3
Explanation: Longest subarray is `[2,3,1]`.

## Approach
- Use sliding window with `left` ,`right` pointers.
- Expand `right` and keep adding to `window_sum`.
- If `window_sum > K`, shrink from `left`.
- Track max length when `window_sum <=k`.

## Complexity
- Time Complexity : O(n)
- Space Complexity : O(1)