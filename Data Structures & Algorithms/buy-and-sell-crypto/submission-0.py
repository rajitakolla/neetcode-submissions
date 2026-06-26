class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        leastBuy = prices[0]

        for price in prices:
            maxPrice = max(maxPrice, price-leastBuy)
            leastBuy = min(leastBuy, price)

        return maxPrice