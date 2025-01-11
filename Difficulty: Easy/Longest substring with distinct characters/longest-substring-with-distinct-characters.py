#User function Template for python3
class Solution:
    def longestUniqueSubstr(self, s):
        start = 0
        maxlen = 0 
        end = 0

        while end < len(s):
            
            k = list(s[start:end + 1])
            if len(set(k)) == len(k):
                maxlen = max(maxlen, end - start + 1)
                end += 1 
            else:
                start += 1  # Shrink the window

        return maxlen


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends