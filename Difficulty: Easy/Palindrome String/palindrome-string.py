#User function Template for python3
class Solution:
    def isPalindrome(self, s: str, start = 0 , end = None ) -> bool:
        if end == None :
            end = len(s)-1 
            
        if start>=end :
            return True 
            
        if s[start]!= s[end]:
            return False
            
        else :
            return self.isPalindrome(s,start+1, end-1 )
            
            
		


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()  # Use lowercase 's'
        ob = Solution()
        answer = ob.isPalindrome(s)
        print("true" if answer else "false")  # Print "true" or "false"
        print("~")

# } Driver Code Ends