#User function Template for python3
class Solution:
    
    def countTriangles(self, arr):
        n=len(arr)
        arr.sort()
        count = 0
        for k in range(2,n):
            start = 0 
            end = k-1 
            
            while start<end :
                if arr[start]+ arr[end] > arr[k] :
                    count+= (end-start)
                    end-=1 
                    
                else :
                    start+=1 
                    
            

        return count
                
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countTriangles(arr))

        print("~")

# } Driver Code Ends