#User function Template for python3

class Solution:
    def factorial(self, n):
        if n == 0 :
            return 1 
        else :
            return n*self.factorial(n-1)
            
    def factorialNumbers(self, n):
    	#code here
    	result = []
    	k = 1
    	fact = 1
    	
    	while(fact <= n):
    	    result.append(fact) 
    	    k+=1 
    	    fact = self.factorial(k) 
    	    
    	return result
    	


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends