#User function Template for python3

class Solution:
    def fn(self, ind, arr, ans, ds):
        
        ans.append(ds[:])
        
        for i in range(ind, len(arr)):
            if i != ind and arr[i]==arr[i-1]:
                continue 
            
            ds.append(arr[i])
            self.fn(i+1, arr, ans, ds)
            ds.pop() 
            
        
    def printUniqueSubset(self, nums):
        # Code here
        nums.sort()
        ans=[]
        ds=[]
        self.fn(0, nums, ans, ds)
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution()
        res = ob.printUniqueSubset(nums)
        print('[ ', end='')
        for subset in res:
            print('[ ', end='')
            for val in subset:
                print(val, end=' ')
            print(']', end='')
        print(' ]')
        print("~")

# } Driver Code Ends