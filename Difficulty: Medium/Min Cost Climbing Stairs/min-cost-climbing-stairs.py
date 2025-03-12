#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        
        n = len(cost) 
        
        # recursion
        
        '''
        
        def fn(ind) :
            if ind <= 1 :
                return 0 
            lt = fn(ind-1)+ cost[ind-1]
            
            rt = fn(ind-2) + cost[ind-2]
                
            return min(lt, rt) 
        '''
        
        # optimized 
        
        prev1, prev2 = 0, 0 
        
        for i in range(2, n+1) :
            cur = min(prev1 + cost[i-1] , prev2 + cost[i-2])
            prev2, prev1 = prev1 , cur 
        
        return prev1
        
        
        


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends