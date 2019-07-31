def isLeaf (self, x: TreeNode) -> bool: 
        return x and (x.left == x.right == None)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        rightVal = self.sumOfLeftLeaves(root.right) 
        leftVal = root.left.val if self.isLeaf(root.left) else self.sumOfLeftLeaves(root.left)   
        return rightVal + leftVal