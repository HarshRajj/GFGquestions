class Solution:
	def minJumps(self, arr):

        ans = 0
        max_ind = 0
        ind = 0
        
        for i in range(len(arr)):
            if i > ind:
                if max_ind < i:
                    return -1
                ind = max_ind
                ans += 1
            max_ind = max(max_ind, i + arr[i])
        
        return ans

	    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends