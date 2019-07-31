res = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        self.length(root)
        return self.res 
        
    def length(self, x: TreeNode) -> int:
        if x == None:
            return 0
        l = self.length(x.left)
        r = self.length(x.right)
        al, ar = 0,0
        if x.left != None and x.left.val == x.val:
            al += l+1
        if x.right != None and x.right.val == x.val:
            ar += r+1
        self.res = max(self.res, al+ar)
        return max(al,ar)