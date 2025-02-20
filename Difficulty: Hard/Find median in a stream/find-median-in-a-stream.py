
import heapq
class Solution:
    def getMedian(self, arr):
        ans, maxheap , minheap = [],[],[] 
        
        heapq.heappush(maxheap,-arr[0])
        ans.append(arr[0]/1)
        
        for i in range(1,len(arr)) :
            
            if maxheap and -maxheap[0]<arr[i] :
                heapq.heappush(minheap, arr[i]) 
            else:
                heapq.heappush(maxheap, -arr[i]) 
                
            if len(maxheap)> len(minheap)+1 :
                t = -heapq.heappop(maxheap)
                heapq.heappush(minheap, t)
                
            elif len(minheap) > len(maxheap) :
                heapq.heappush(maxheap, -heapq.heappop(minheap))
                
            if len(maxheap)>len(minheap):
                ans.append(-maxheap[0])
            else :
                ans.append((-maxheap[0]+minheap[0])/2)
                
        return ans
        
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.getMedian(nums)
        print(" ".join(f"{x:.1f}" for x in ans))


if __name__ == "__main__":
    main()

# } Driver Code Ends