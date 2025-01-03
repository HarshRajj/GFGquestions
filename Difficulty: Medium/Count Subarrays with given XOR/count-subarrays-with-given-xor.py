class Solution:
    def subarrayXor(self, arr, k):
        
        xr = 0 
        cnt = 0 
        dic = {0:1}
        
        for num in arr :
            xr = xr ^ num 
            x = xr ^ k
            if x in dic :
                cnt += dic[x] 
            if xr in dic :
                dic[xr]+=1 
            else :
                dic[xr] = 1 
                
        return cnt 
        
        
        
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends