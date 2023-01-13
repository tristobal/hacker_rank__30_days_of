"""
Binary Search Trees

Task
The height of a binary search tree is the number of edges between the tree's root and its furthest leaf.
You are given a pointer, root, pointing to the root of a binary search tree. Complete the getHeight function provided
in your editor so that it returns the height of the binary search tree.

Input Format
The locked stub code in your editor reads the following inputs and assembles them into a binary search tree:
The first line contains an integer, n, denoting the number of nodes in the tree.
Each of the n subsequent lines contains an integer, data, denoting the value of an element that must be added
to the BST.


Output Format
The locked stub code in your editor will print the integer returned by your getHeight function denoting the height of
the BST.
"""


class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data


class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        aux = self.get_height_with_nodes(root)
        if aux == 0:
            return 0
        else:
            return aux - 1

    def get_height_with_nodes(self, root):
        if root is None:
            return 0
        return max(self.get_height_with_nodes(root.left), self.get_height_with_nodes(root.right)) + 1

T=int(input())