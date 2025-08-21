#  Day 3 -Prefix Sum

Prefix sum is a technique to preprocess an array so that we can quickly compute sums of subarrays.

---

### Problem Solved:
1. **Find Pivot Index** 
 - Find the index where the sum of hte numbers to the left is equal to the sum of the numbers to the right.

2. **Range Sum Query (immutable)** 
 - Precompute prefix sums to answer subarray sum queries in o(1) time.

3. **Subarray Sum equals k**
 - Use prefix sums_hashmap to count how many subarrays have  a sum equal to `k`.

### Key Learnings:
 - Perfix sums help reduces repeated computation.
 - Using extra space (prefix array or hashmap)-> we trade space for speed.
 - Problems like subarray sums, pivot index, range queries become efficient with this approach.