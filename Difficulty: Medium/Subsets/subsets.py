#User function Template for python3

class Solution:
    def fn (self, ind, arr, ans, ds):
        
        ans.append(ds[:])
        '''
        ds.append(arr[ind]) 
        self.fn(ind+1, arr, ans, ds) 
        
        ds.pop()
        while ind + 1 < len(arr) and arr[ind] == arr[ind + 1]:
            ind += 1
        
        self.fn(ind+1, arr, ans, ds)
        '''
        
        for i in range(ind, len(arr)):
            if i!=ind and arr[i]==arr[i-1] :
                continue 
            ds.append(arr[i])
            self.fn(i+1, arr, ans, ds)
            ds.pop()
                
            
        
    def subsets(self, arr):
        # code here
        arr.sort()
        ans = []
        ds = [] 
        self.fn(0, arr, ans, ds) 
        return ans


#{ 
 # Driver Code Starts
# Example to simulate input/output behavior:
if __name__ == "__main__":
    t = int(input())  # Number of test cases
    for _ in range(t):
        arr = list(map(int,
                       input().split())
                   )  # Reading the array input as space-separated integers

        ob = Solution()
        res = ob.subsets(arr)

        # Print result
        for subset in res:
            if len(subset) == 0:
                print("[]")
            else:
                for num in subset:
                    print(num, end=" ")
                print()

        print("~")

# } Driver Code Ends