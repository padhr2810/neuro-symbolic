"""
TRICK #1: 
KEEP TRACK OF 2 VARIABLES, 1: THE MINIMUM PRICE OBSERVERED THUS FAR
			   2: THE MAX PROFIT THUS FAR
JUST RETURN THE SECOND VAR, I.E. MAX PROFIT... (DON'T BOTHER STORING THE INDICES)

TRICK #2: INIT THE MIN VALUE AS INFINITY, AND THE MAX PROFIT THUS FAR AS ZERO.
"""

from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:

    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
