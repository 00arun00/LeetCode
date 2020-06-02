class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
            Inverts a binary tree 

            Args:
                root : (TreeNode) the root of the binary tree
            
            Returns:
                root : (TreeNode) the root of the inverted binary tree
        
        ----------------------------------------------------------------

            Space Complexity: O(1)
            Time Complexity: O(n)

            Key Concepts:
                - recursion 
                - tree traversal

        """

        self.rec_invert(root)
        return root

    def rec_invert(self,node):
        """
            recursive funciton to invert a binary tree
            Args:
                node : (TreeNode) 
            
            Returns:
                None
        """
        if node:
            node.left, node.right = node.right, node.left
            self.rec_invert(node.left)
            self.rec_invert(node.right)

