# Intuition:
# To maximize profit we want to buy at the lowest price seen so far and
# sell at a later, higher price. While scanning the prices once, we keep
# track of the cheapest price so far. At each day, the best profit if we
# sell today is today's price minus that minimum.
#
# Approach:
# 1. Initialize buy_price to a very large value and profit to 0.
# 2. Loop over each price in prices.
# 3. If price < buy_price, we found a cheaper day to buy, so update
#    buy_price.
# 4. Otherwise, compute the profit of selling today (price - buy_price)
#    and keep the maximum in profit.
# 5. After the loop, return profit. If prices only decrease, no
#    profitable trade exists and profit stays 0.
#
# Complexity:
# Time:  O(n) -- a single pass over the prices.
# Space: O(1) -- only two variables are used.

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy_price = 1000000
        profit = 0
        for price in prices:
            if price < buy_price:
                buy_price = price
            else:
                profit = max(profit, price - buy_price)
        return profit