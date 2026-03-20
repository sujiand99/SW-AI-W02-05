# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def visiting(self, node):
        if not node:
            return 0
        
        max_depth = max(self.visiting(node.left), self.visiting(node.right))
        return max_depth + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return(self.visiting(root))