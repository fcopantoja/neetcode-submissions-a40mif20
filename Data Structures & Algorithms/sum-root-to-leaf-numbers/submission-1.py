# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbersNaive(self, root: Optional[TreeNode]) -> int:
        result = []
        def dfs(node, path):
            if not node.left and not node.right:
                path += str(node.val)
                result.append(path)
                return
            
            if node.left:
                dfs(node.left, path + str(node.val))
            if node.right:
                dfs(node.right, path + str(node.val))
        
        dfs(root, "")
        return sum([int(x) for x in result])

    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum = curr_sum * 10 + node.val

            if not node.left and not node.right:
                return curr_sum

            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        
        return dfs(root, 0)