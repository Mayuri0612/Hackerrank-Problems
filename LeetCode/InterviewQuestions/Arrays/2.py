# Best time to buy andsell stocks   
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 0:
            return 0;
        i=0
        while( i < len(prices)-1):
            
            while (( i < len(prices)-1) and (prices[i] >= prices[i+1])):
                i += 1
            if ( i == len(prices)-1):
                break    
            buy = i
            i +=1
        
            while (( i < len(prices)) and (prices[i] >= prices[i-1])):
                i += 1            
            sell = i-1
            new = (prices[sell] - prices[buy])
            profit = profit + new
        return profit