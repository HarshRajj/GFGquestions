class Solution:
    
    def canWePlace (self, arr, dist, k):
        
        last = arr[0] 
        cows= 1
        for i in range(1,len(arr)):
            if arr[i]-last >= dist : 
                cows += 1
                last = arr[i] 
                
        if cows >= k :
            return True 
        else :
            return False
                

    def aggressiveCows(self, stalls, k):
        # your code here
        
        stalls.sort()
        
        low = 1
        high = max(stalls) - min(stalls)
        
        while low <= high :
            mid = ( low + high )//2 
            if self.canWePlace( stalls, mid, k) :
                low = mid+1
            else :
                high = mid-1
                
        return high



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends