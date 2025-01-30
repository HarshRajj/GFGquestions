#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        def is_safe(board, row, col):
            for c in range(col):
                if board[c] == row or abs(board[c] - row) == abs(c - col):
                    return False
            return True

        def backtrack(board, col):
            if col == n:
                results.append(board[:])  # Store a valid solution
                return
            for row in range(1, n + 1):  # 1-based index
                if is_safe(board, row, col):
                    board[col] = row
                    backtrack(board, col + 1)
                    
        results = []
        board = [0] * n  # To store queen positions in each column
        backtrack(board, 0)
        return results 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends