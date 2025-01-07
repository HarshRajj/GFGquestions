#User function Template for python3


class Solution:
    def countPairs (self, arr, target) : 
        #Complete the function
        dic = {}
        count = 0
        for num in arr :
            comp = target - num 
            
            if comp in dic :
                count+= dic[comp] 
                
            if num in dic :
                dic[num]+= 1 
            else :
                dic[num] = 1 
                
        return count
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        arr = list(map(int, data[index].strip().split()))
        index += 1
        target = int(data[index].strip())
        index += 1

        res = Solution().countPairs(arr, target)
        print(res)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends