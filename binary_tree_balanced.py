##############################
# Binary Trees
# 
# Author: Drew Fisher
# Started: 6/13/18
##############################

# Binary Tree Node class
class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

# isSuperbalanced
#
# A binary tree is superbalanced if no two nodes have a difference
#     in depth greater than 1.
# Inputs: BinaryTreeNode (binary tree)
# Returns: True if balanced, False if not
def superBalancedHelper(binaryTree, depth, depths):
    if (binaryTree.left == None and binaryTree.right == None):
        if depth not in depths:
            depths.append(depth);
    if (binaryTree.left):
        superBalancedHelper(binaryTree.left, depth + 1, depths);
    if (binaryTree.right):
        superBalancedHelper(binaryTree.right, depth + 1, depths);
    if ((len(depths) > 2) or\
        (len(depths) == 2 and abs(depths[0] - depths[1]) > 1)):
                return False
    else:
        return True

def isSuperbalanced(binaryTree):
    isBalanced = superBalancedHelper(binaryTree, depth = 0, depths = []);
    return isBalanced

#Tests

#    5
# Is superbalanced
bt = BinaryTreeNode(5);
print(isSuperbalanced(bt));

#    5
#   / \
#  2   3
#   \
#    4
#   /
#  1
# Not superbalanced
bt = BinaryTreeNode(5);
l1 = bt.insert_left(2);
r1 = bt.insert_right(3);
l2 = l1.insert_right(4);
r2 = l2.insert_left(1);

print(isSuperbalanced(bt));
