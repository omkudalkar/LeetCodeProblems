
def maxProfit(prices) -> int:
    i = 0
    max_profit = 0 
    while i < len(prices):
        j = i+1
        while j < len(prices):
            curr_profit = prices[j] - prices[i]
            if (curr_profit) > max_profit:
                max_profit = curr_profit
            j+=1
        i+=1
    return max_profit

def tester():
    assert (maxProfit([7,1,5,3,6,4])) == 5
    assert (maxProfit([7,6,4,3,1])) == 0
    assert (maxProfit([1,2,3,4,5])) == 4


def main():
    tester()
    
main()

