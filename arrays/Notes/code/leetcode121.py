class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update minimum price so far
            if price < min_price:
                min_price = price
            # Calculate profit if sold today
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
                
        return max_profit

# Example usage
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print("Maximum Profit:", Solution().maxProfit(prices))  # Output: 5