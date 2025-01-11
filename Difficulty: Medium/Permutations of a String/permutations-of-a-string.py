#User function Template for python3

class Solution: 

    def findPermutation(self, s): 
        
        def backtrack(ind):
            if ind == len(nums):
                res.append(''.join(nums))
                return
            
            used = set()
            for i in range(ind, len(nums)):
                if nums[i] in used: 
                    continue
                used.add(nums[i])
                nums[ind], nums[i] = nums[i], nums[ind]
                backtrack(ind + 1)
                nums[ind], nums[i] = nums[i], nums[ind]
                
        nums = sorted(list(s)) 
        res = [] 
        backtrack(0) 
        return res 
        
        
        
        

        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends