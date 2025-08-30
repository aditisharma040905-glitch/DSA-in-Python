# Day 1 – Big-O Notation + Two Sum Problem

## 1. Big-O Notation (Time & Space Complexity)

- **What is Big-O?**
  Big-O notation tells us how the runtime of an algorithm grows as input size increases.

- **Why it matters?**
  Helps compare which algorithm is faster and more efficient for large inputs.

### Common Complexities
| Complexity | Name            | Example                              |
|------------|-----------------|--------------------------------------|
| O(1)       | Constant        | Accessing first element of list      |
| O(log n)   | Logarithmic     | Binary Search                        |
| O(n)       | Linear          | Looping through an array             |
| O(n log n) | Linearithmic    | Merge Sort, Quick Sort (average)     |
| O(n²)      | Quadratic       | Nested loops (e.g., Bubble Sort)     |

---

## 2. Problem: Two Sum (LeetCode 1)

### Problem Statement
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`.

### Example
Input: `nums = [2,7,11,15], target = 9`  
Output: `[0,1]` (since `nums[0] + nums[1] = 2 + 7 = 9`)

---

## 3. Solution Approaches

### Approach 1: Brute Force (O(n²))
- Check every pair of numbers.
- If their sum == target, return indices.

### Approach 2: Hash Map (O(n))
- Use a dictionary to store numbers we have seen.
- For each number, check if `target - num` already exists in the dictionary.
- If yes → return indices.

---

