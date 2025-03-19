class Solution:
    def maxProfit(self, arr , k):
        
        n = len(arr)
        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]

        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, k + 1):
                    if buy == 1:
                        dp[ind][buy][cap] = max(-arr[ind] + dp[ind + 1][0][cap], dp[ind + 1][1][cap])
                    else:
                        dp[ind][buy][cap] = max(arr[ind] + dp[ind + 1][1][cap - 1], dp[ind + 1][0][cap])

        return dp[0][1][k]



#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends