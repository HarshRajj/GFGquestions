#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3

class Solution:
    def countPairs(self, arr, target):
        arr.sort()  # Step 1: Sort the array
        count = 0
        start, end = 0, len(arr) - 1
        
        while start < end:
            if arr[start] + arr[end] < target:
                # All pairs from `start` to `end-1` are valid
                count += (end - start)
                start += 1  # Move the `start` pointer
            else:
                end -= 1  # Move the `end` pointer
            
        return count

        
        
        

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends