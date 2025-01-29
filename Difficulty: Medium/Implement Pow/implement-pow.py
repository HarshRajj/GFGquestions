#{ 
 # Driver Code Starts
#Initial Template for Python 3


# } Driver Code Ends
#User function Template for python3
class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        sign = 0
        if e<0:
            sign = -1 
        
        e = abs(e)
            
        x = 1 
        while (e>0):
            if e%2 == 1 :
                x = x*b
            b= b*b
            e = e//2 
            
        if sign ==-1:
            return 1/x
        else:
            return x
            

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        b = float(input())
        e = int(input())
        ob = Solution()
        result = ob.power(b, e)
        print(f"{result:.5f}")
        print("~")
# } Driver Code Ends