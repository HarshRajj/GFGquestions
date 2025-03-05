#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def longestStringChain(self, words):
        words.sort(key = len) 
        dic= {}
        
        for k in words :
            dic[k] = 1 
            for i in range (len (k)):
                prd = k[:i] + k[i+1 :]
                if prd in dic :
                    dic[k] = max(dic[k], dic[prd]+1)
                    
        return max(dic.values())
                


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends