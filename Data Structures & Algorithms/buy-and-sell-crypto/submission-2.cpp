class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int maxP = 0;
        int profit = 0;

        while (r < prices.size()) {
            if (prices[r] < prices[l]) {
                l = r;
            } else {
                profit = prices[r] - prices[l];

                if (profit > maxP) {
                    maxP = profit;
                }
            }

            r++;
        }

        return maxP;
    }
};
