class Solution:
    def isWordExist(self, mat, word):
        def check(mat, i, j, ind, word, visited):
            if ind == len(word):
                return True

            # Check boundaries and other conditions
            if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]) or visited[i][j] or mat[i][j] != word[ind]:
                return False

            visited[i][j] = True

            # Explore all 4 directions
            if (check(mat, i, j + 1, ind + 1, word, visited) or
                check(mat, i, j - 1, ind + 1, word, visited) or
                check(mat, i - 1, j, ind + 1, word, visited) or
                check(mat, i + 1, j, ind + 1, word, visited)):
                return True

            # Backtracking
            visited[i][j] = False
            return False

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == word[0]:
                    visited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
                    if check(mat, i, j, 0, word, visited):
                        return True

        return False

		


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends