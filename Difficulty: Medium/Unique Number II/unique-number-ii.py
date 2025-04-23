#User function Template for python3

class Solution:
	def singleNum(self, arr):
		# Code here
		ans = [] 
		dic = {} 
		for num in arr :
		    dic[num] = dic.get(num, 0)+1 
		for k in dic :
		    if dic[k] == 1 :
		        ans.append(k)
		return sorted(ans)
		        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends