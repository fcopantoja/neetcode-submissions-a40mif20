# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        result = []
        left = True

        while queue:
            level = deque()
            for i in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                if left:
                    level.append(node.val)
                if not left:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if level:
                result.append(list(level))
            left = not left

        return result

