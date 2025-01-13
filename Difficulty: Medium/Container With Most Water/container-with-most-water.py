
class Solution:
    def maxWater(self, arr):
        
        lt = 0 
        rt = len(arr)-1
        wtr = 0
        maxi = 0
        
        while lt < rt :
            
            height = min(arr[lt], arr[rt]) 
            wtr = height * (rt - lt) 
            
            if wtr>maxi :
                maxi = wtr 
                
            if arr[lt] < arr[rt] :
                lt+=1 
            else :
                rt-=1 
                
        return maxi
            
            
            
                        
        


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