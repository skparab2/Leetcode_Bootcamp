# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        # print(root)

        # lets do level order traversal

        allVals = []

        allNodes = []

        nodequeue = [root]

        currentIndex = 0

        numActual = 1
        numNone = 0

        i = 0
        while (numActual > 0):
            currentnode = nodequeue[currentIndex]
            nodequeue[currentIndex] = None
            

            if (len(nodequeue) > 300 == 0):
                nodequeue = nodequeue[currentIndex:]
                currentIndex = 0

            if (currentnode != None):
                allVals.append(currentnode.val)
                allNodes.append(currentnode)
                
                numActual -= 1
                
                nodequeue.append(currentnode.left)
                nodequeue.append(currentnode.right)

                if (currentnode.left == None):
                    numNone += 1
                else:
                    numActual += 1

                if (currentnode.right == None):
                    numNone += 1
                else:
                    numActual += 1

            else:
                allVals.append(None)
                nodequeue.append(None)
                nodequeue.append(None)

                numNone += 1

            currentIndex += 1
                
            i += 1


        # print(allVals)

        # now, find p and then backtrack

        indexP = allVals.index(p.val)

        ancestorsP = {}

        while (indexP != 0):
            ancestorsP[allVals[indexP]] = 0

            indexP = int(math.floor((indexP-1)/2))

        ancestorsP[allVals[0]] = 0

        # print(ancestorsP)

        indexQ = allVals.index(q.val)

        while (indexQ != 0):
            if (allVals[indexQ] in ancestorsP):
                break

            indexQ = int(math.floor((indexQ-1)/2))
        
        index = 0
        while (index < len(allNodes)):
            if (allNodes[index].val == allVals[indexQ]):
                return allNodes[index]
            index += 1
