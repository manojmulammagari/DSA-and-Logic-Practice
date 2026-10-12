class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf') # Set initially to infinity
        max_profit = 0
        
        for price in prices:
            # If we find a lower price, update our buying price
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today gives us a better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit