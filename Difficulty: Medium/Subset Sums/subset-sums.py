#User function Template for python3
class Solution:
    
    def fn(self, ind, arr , s , ans ) :
        
        n = len(arr) 
        if ind == n :
            ans.append(s) 
            return 
    
        self.fn(ind+1, arr, s+arr[ind], ans ) 
        self.fn(ind+1, arr, s, ans)
        
            
            
	def subsetSums(self, arr):
	    
	    ans = [] 
	    s = 0 
	    self.fn (0, arr, s, ans )
	    return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        arr = [int(x)
               for x in input().split()]  # Reading array for the test case
        ob = Solution()
        ans = ob.subsetSums(arr)  # Getting the subset sums
        ans.sort()  # Sorting the result

        # Printing the subset sums in space-separated format
        for x in ans:
            print(x, end=" ")
        print("")  # Ensuring new line after each test case

# } Driver Code Ends