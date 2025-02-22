
class Solution:
    def maxLength(self, s):
        
        max_length = 0
                
        l,r=0,0        
        
        for i in range(len(s)):
            if s[i] == '(':
                l+=1
            else:
                r+=1                        
            if l == r:
                max_length=max(max_length, l*2)
            elif r>l:
                l=r=0
        
        l,r=0,0        
        
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                l+=1
            else:
                r+=1            
            if l == r: 
                max_length=max(max_length, l*2)
            elif l>r:
                l=r=0
        return max_length
        


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends