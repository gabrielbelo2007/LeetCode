#include <string.h>
#include <limits.h>

int maxProfit(int* prices, int pricesSize) {
    if (pricesSize > 1)
    {
        int min_price = INT_MAX;
        int max_profit = 0;

        int transactions = 0;
        for (int buy_value = 0; buy_value < pricesSize; buy_value++)
        {
            if (prices[buy_value] < min_price)
            {
                min_price = prices[buy_value];
            }

            transactions = prices[buy_value] - min_price;

            if (transactions > max_profit)
            {
                max_profit = transactions;
            }
        }
        return max_profit;
    }
    return 0;
}