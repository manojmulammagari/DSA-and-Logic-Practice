class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        minprice=prices[0]
        max_profit=0

        for i in range(1,len(prices)):
            if prices[i] <minprice:
                minprice=prices[i]

            elif (prices[i]-minprice)>max_profit:
                
                max_profit=prices[i]-minprice
                


        return max_profit




            
        

