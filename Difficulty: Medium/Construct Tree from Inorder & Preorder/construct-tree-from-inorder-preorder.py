#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    
    def fn ( self,mp, preorder, preInd, left, right ):
        
        if left > right :
            return None
            
        rootval = preorder[preInd[0]]
        preInd[0] += 1
        
        root = Node(rootval)
        ind = mp[rootval]
        
        root.left = self.fn(mp, preorder, preInd, left, ind-1)
        root.right = self.fn(mp, preorder, preInd, ind+1, right)
        
        return root
        
        
        
    def buildTree(self, inorder, preorder):
        # code here
        mp = {value : idx for idx, value in enumerate(inorder) }
        preInd= [0]
        
        return self.fn(mp, preorder, preInd, 0, len(inorder)-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inorder = [int(x) for x in input().split()]
        preorder = [int(x) for x in input().split()]

        root = Solution().buildTree(inorder, preorder)
        printPostorder(root)
        print()

# } Driver Code Ends