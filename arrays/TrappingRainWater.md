# Day 8 - Trapping Rain Water

## Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example
Input Height=[0,1,0,2,1,0,1,3,2,1,2,1]
Output = 6

---
## Approach - Two Pointer Technique
1. We Maintain two pointers: `left` at the beginning and `right` at the end.
2. Keep track of the maximum height seen so far from the left (`left_max`) and from the right (`right_max`).
3. Move the pointer which has the smaller current height:
- If `height[left] < height[right]`, then check if water cab be trapped using `left_max`.
- Otherwise, check using `right_max`.
4. Continue until `left` meets `right`.

This works because at every step, the trapped water depends on the **minimum of left_max and right_max**.

---

**Time Complexity** -O(n)
**Space Complexity**- O(1)

---
# Dry Run
For height = `[0,1,0,2,1,0,1,3,2,1,2,1]`

- Water trapped = 6 units  
  - (between indices 2–3, 4–5, 5–6, 8–9, etc.)