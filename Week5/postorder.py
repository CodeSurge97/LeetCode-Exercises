def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root:
            for child in root.children:
                res += self.postorder(child)
            res.append(root.val)
        return res