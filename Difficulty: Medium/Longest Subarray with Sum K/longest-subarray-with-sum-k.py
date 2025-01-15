# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        
        mpp = {0:-1} 
        summ = 0 
        maxlen = 0
        for i in range(len(arr)) :
            summ += arr[i] 
            x = summ-k 
            if x in mpp :
                maxlen = max(maxlen, i-mpp[x]) 
                
            
            if summ not in mpp:
                mpp[summ] = i
                
        return maxlen       
    
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends