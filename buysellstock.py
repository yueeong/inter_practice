#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

class Solution():
    def __init__(self):
        pass
    def getmaxprofit(self, price_list):
        self.profit = 0
        for bidx,buyprice in enumerate(price_list):
            left_limit = bidx+1
            print("max profit so far:",self.profit)
            for i in range(left_limit,len(price_list)):
                prof_this_round = price_list[i] - buyprice
                if prof_this_round > 0 and prof_this_round > self.profit:
                    self.profit = prof_this_round          
        print(self.profit)


def main():
    soln = Solution()
    soln.getmaxprofit([7,5,3,1,6,4,9,10,12])

if __name__ == "__main__":
    main()

        