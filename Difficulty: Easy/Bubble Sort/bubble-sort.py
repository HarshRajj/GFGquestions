#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr):
        # code here
        for i in range(len(arr)-1):
            bub = arr[i]
            for j in range(i+1,len(arr)):
                if arr[i]>arr[j] :
                    arr[j], arr[i] = arr[i], arr[j] 
                    bub = arr[j]
                    
        return
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends