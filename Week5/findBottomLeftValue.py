def bfs(self, root, result, level):
        if root is None:
            return
        if len(result) <= level:
            result.append(root.val)
        self.bfs(root.left, result, level+1)
        self.bfs(root.right, result, level+1)
    
    def findBottomLeftValue(self, root: TreeNode) -> int:
        result = []
        level = 0
        self.bfs(root, result, level)
        return result[-1]