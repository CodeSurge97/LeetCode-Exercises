 def Leaf (self, x: TreeNode, leaves: List[int]):
        if x != None:
            if x.left == x.right == None:
                leaves.append(x.val)
            self.Leaf(x.left, leaves)
            self.Leaf(x.right, leaves)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        res1 = []
        res2 = []
        self.Leaf(root1, res1)
        self.Leaf(root2, res2)
        return res1 == res2 