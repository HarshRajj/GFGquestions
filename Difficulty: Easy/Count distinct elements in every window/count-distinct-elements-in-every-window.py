
class Solution:
    def countDistinct(self, arr, k):
        dic = {}
        ans = [] 
        n = len(arr)
        for i in range(k):
            if arr[i] in dic:
                dic[arr[i]]+=1 
            else:
                dic[arr[i]] = 1 
        ans.append(len(dic))
        
        for j in range(k, n):
            start = arr[j-k]
            
            if dic[start]>0 :
                dic[start]-=1 
                if dic[start]==0 :
                    del dic[start]
                
                    
            if arr[j] in dic:
                dic[arr[j]] += 1  
                

            else:
                dic[arr[j]] = 1  
            
            ans.append(len(dic))    
                
                
        return ans
                
        
        
        


#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends