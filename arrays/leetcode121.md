# Day 5 - Best time to Buy and Sell Stock

## Problem statement
You are given an array `prices` where `prices[i]` is the profit of a stock on the `i`th day.Find the maximum profit you  can achieve by choosing a day to buy and another dayto sell.


## Approach
 - Track the minimum price seen so far.
 - At each day,calculate potential profit =`price -min_price`.
 - Update `max_profit` if profit is higher.
 - Time complexity:O(n),Space complexity: O(1)

# Example
Input:[7,1,5,3,6,4]
Output: 5
