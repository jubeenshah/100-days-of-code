# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level = [root] if root else []
        listToReturn = []
        if not root:
            return []
        while level:
            listToAppend = []
            queue = []
            for eachLevel in level:
                if eachLevel.left:
                    queue.append(eachLevel.left)
                    listToAppend.append(eachLevel.left.val)
                if eachLevel.right:
                    queue.append(eachLevel.right)
                    listToAppend.append(eachLevel.right.val)
            listToReturn.append(listToAppend)
            level = queue
        listToReturn.pop()
        listToReturn.insert(0,[root.val])
        return (listToReturn[::-1])
        #appendValues(root)
        
        
        