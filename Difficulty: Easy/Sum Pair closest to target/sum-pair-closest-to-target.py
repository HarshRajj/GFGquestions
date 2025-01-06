#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        
        arr.sort()
        summ = 0 
        start, end = 0, len(arr)-1 
        closest = float('inf')
        a = 0 
        b = 0
        ans = None
        maxdiff = float('-inf')
        while start<end :
            
            summ  = arr[start] + arr[end ]
            diff = abs(arr[start]-arr[end])
            
            
            if abs(target-closest) > abs(target-summ):
                
                closest = summ
                ans = [arr[start], arr[end]]                    
                maxdiff = diff  
                
            if abs(target-closest) == abs(target-summ): 
                if diff>maxdiff:
                    ans = [arr[start], arr[end]] 
                    maxdiff = diff
                
 
            if summ < target :
                start+=1 
            else :
                end-=1 
                
        return ans
 
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends