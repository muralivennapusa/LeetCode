# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        hm=defaultdict(int)

        def bfs(node,level):
            hm[level]+=node.val

            if node.left:
                bfs(node.left,level+1)
            
            if node.right:
                bfs(node.right,level+1)
        
        bfs(root,1)
        max_key=1
        max_value=hm[1]

        print(hm)

        max_key=max(hm,key=hm.get)

        return max_key