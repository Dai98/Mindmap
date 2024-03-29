from typing import Any
from typing_extensions import Self

# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
current_folder = Path(__file__).parent
sys.path.append(str(current_folder))

from stack import Stack


class BinaryTreeNode:
    def __init__(self, value: Any, left: Self = None, right: Self = None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeTraverse:

    """
        Time Complexity: O(n) - If there are n nodes in binary tree, each node will be accessed for 3 times, therefore 3n times in total, which is O(n)
        Space Complexity: O(h) - If the height of the binary tree is h, then we need h extra space at most to store the route from current node to the root
    """

    def __init__(self) -> None:
        raise NotImplementedError("binary_tree.py-BinaryTreeTraverse/All methods in this class are static. Do not instantiate this class.")
    
    @staticmethod
    def preorder_traverse_recursive(node: BinaryTreeNode) -> None:
        if node is None:
            return
        print(node.value, end=" ")
        BinaryTreeTraverse.preorder_traverse_recursive(node.left)
        BinaryTreeTraverse.preorder_traverse_recursive(node.right)

    @staticmethod
    def inorder_traverse_recursive(node: BinaryTreeNode) -> None:
        if node is None:
            return
        BinaryTreeTraverse.preorder_traverse_recursive(node.left)
        print(node.value, end=" ")
        BinaryTreeTraverse.preorder_traverse_recursive(node.right)

    @staticmethod
    def postorder_traverse_recursive(node: BinaryTreeNode) -> None:
        if node is None:
            return
        BinaryTreeTraverse.preorder_traverse_recursive(node.left)
        BinaryTreeTraverse.preorder_traverse_recursive(node.right)
        print(node.value, end=" ")

    @staticmethod
    def preorder_traverse_nonrecursive(node: BinaryTreeNode) -> list:
        preorder_traverse = []
        if node is None:
            return preorder_traverse
        stack = Stack()
        stack.push(node)
        while stack.size != 0:
            node = stack.pop()
            preorder_traverse.append(node.value)
            if node.right is not None:
                stack.push(node.right)
            if node.left is not None:
                stack.push(node.left)
        return preorder_traverse

    @staticmethod
    def inorder_traverse_nonrecursive(node: BinaryTreeNode) -> list:
        inorder_traverse = []
        if node is None:
            return inorder_traverse
        stack = Stack()
        stack.push(node)
        while stack.size != 0:
            while node is not None:
                stack.push(node.left)
                node = node.left
            node = stack.pop()
            inorder_traverse.append(node.left)
            stack.push(node.right)
        return inorder_traverse

    @staticmethod
    def postorder_traverse_nonrecursive_two_stacks(node: BinaryTreeNode) -> None:
        postorder_traverse = []
        if node is None:
            return postorder_traverse
        stack = Stack()
        collect_stack = Stack()
        stack.push(node)
        while stack.size != 0:
            node = stack.pop()
            collect_stack.push(node)
            if node.left is not None:
                node.push(node.left)
            if node.right is not None:
                node.push(node.right)
        
        while collect_stack.size != 0:
            node = collect_stack.pop()
            postorder_traverse.append(node.value)
        return postorder_traverse
    
    @staticmethod
    def postorder_traverse_nonrecursive_one_stack(node: BinaryTreeNode) -> None:
        postorder_traverse = []
        if node is None:
            return postorder_traverse
        stack = Stack()
        stack.push(node)
        # node is the root node initially
        # Once any node is added to the traverse list
        # node variable stands for the last node being added
        while stack.size != 0:
            cur = stack.peek()
            # When left child is not None and not added
            if cur.left is not None and node != cur.left and node != cur.right:
                stack.push(cur.left)
            # When right child is not None and not added
            elif cur.right is not None and node != cur.right:
                stack.push(cur.right)
            # Both child nodes have been added, only then this current node can be added
            else:
                postorder_traverse.append(cur.value)
                node = stack.pop()

        return postorder_traverse
