import heapq
class Solution:
    
    def maxOfSubarrays(self, arr, k ):
        pq = [] 
        result = []
        n = len(arr)

        
        for i in range(k):
            heapq.heappush(pq , (-arr[i], i))
        result.append(-pq[0][0]) 

        
        for i in range(k, n):
            heapq.heappush(pq, (-arr[i], i))

            
            while pq[0][1] <= i - k:
                heapq.heappop(pq)

            result.append(-pq[0][0]) 

        return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        res = ob.maxOfSubarrays(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")
# } Driver Code Ends