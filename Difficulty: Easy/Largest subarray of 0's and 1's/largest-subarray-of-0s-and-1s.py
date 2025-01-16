class Solution:
    def maxLen(self, arr):
        # code here
        
        n = len(arr)
        sum = 0
        mpp = {0:-1} 
        maxlen = 0
        for i in range(n):
            sum += arr[i] if arr[i] == 1 else -1
            
            if sum in mpp :
                maxlen = max(maxlen, i-mpp[sum]) 
                
            else :
                mpp [sum] = i
                
        return maxlen
        
                
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends