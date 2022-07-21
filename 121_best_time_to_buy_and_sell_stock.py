def maxProfit(prices) -> int:
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)

        max_profit = max(max_profit, price - min_price)

    return max_profit

prices = [2, 4, 1]

print(maxProfit(prices))