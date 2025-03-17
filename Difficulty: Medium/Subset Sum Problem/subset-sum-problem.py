class Solution:
    def isSubsetSum (self, arr, target):
        n = len(arr)
        dp = [False] * (target + 1)
        dp[0] = True 
    
        for num in arr:
            for j in range(target, num - 1, -1):
            
                dp[j] = dp[j] or dp[j - num]
    
        return dp[target]
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Endshttps://media.geeksforgeeks.org/img-practice/chatIcon-1653561581.svg