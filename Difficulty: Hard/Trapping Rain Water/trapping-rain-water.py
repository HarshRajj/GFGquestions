
class Solution:
    def maxWater(self, arr):
        # code here
        
        n = len(arr) 
        leftm = [0]*n 
        rightm = [0]*n
        water = 0 
        for i in range(1,n):
            leftm[i] = max(arr[i-1],leftm[i-1]) 
            
        for i in range(n-2, -1, -1):
            rightm[i] = max(arr[i+1], rightm[i+1])
            
        for i in range(n):
            mini = min(leftm[i],rightm[i])
            if mini > arr[i] :
                water += mini - arr[i]
        
        return water              
            
        
        


#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends