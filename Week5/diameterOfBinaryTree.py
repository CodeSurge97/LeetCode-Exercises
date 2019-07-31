  res = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 1
        self.depth(root)
        return self.res - 1
        
    def depth(self, x: TreeNode) -> int:
        if x == None:
            return 0
        l = self.depth(x.left)
        r = self.depth(x.right)
        self.res = max(self.res, l+r+1)
        return max(l,r) + 1