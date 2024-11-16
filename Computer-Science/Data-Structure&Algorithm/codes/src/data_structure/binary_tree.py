from typing import Any, List, Optional
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
            inorder_traverse.append(node.value)
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


class LevelTraversal:
    """
    Given root of a binary tree, return level order traversal of its nodes' values (Leetcode 102)
    BFS of binary tree, can use this as the BFS template of binary tree

    Args:
        root (Optional[BinaryTreeNode]) - root node of a binary tree
    Return:
        A list of list, whose elements are the node values on each level
    """
    def level_order(self, root: Optional[BinaryTreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = [root]
        while queue:
            # Current queue length is the number of nodes in this level
            # Because as nodes are poping and appending
            # Nodes of last levels will be all poped, and only leave nodes of next level
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level)
        return result
    

class ZigzagTraversal:
    """
    Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
    (i.e., from left to right, then right to left for the next level and alternate between) (Leetcode 103)

    Variation of BFS of binary tree
    Use a boolean flag to control whether to reverse level node value, and flip the boolean value at the end of every level
    In every level, iterate nodes to get value first (reverse if flag is true), then pop nodes and add child nodes to queue later

    Args:
        root (Optional[BinaryTreeNode]) - root node of a binary tree
    Return:
        A list of list, whose elements are the node values on each level, in zigzag order
    """
    def zigzag_level_order(self, root: Optional[BinaryTreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        result = []
        # When reverse = True, get node value from right to left, otherwise from left to right
        reverse = False
        while queue:
            level_size = len(queue)
            # Get the node values of this level first
            level = [node.val for node in queue]
            # Reverse if boolean flag is True
            if reverse:
                level = level[::-1]
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level)
            # Flip boolean flag at the end of each level
            reverse = not reverse
        return result
    

class BinaryTreeWidth:
    """
    Calculate the maximum width of each level in a given binary tree
    Width is the number of nodes between the first and last non-null binary tree nodes (including null nodes) (Leetcode 662)

    Variation of BFS of Binary tree
    On each level, instead of gathering nodes' value, calculate the width of this level, and keep the maximum level width throughout traversal
    
    In order to quickly calculating how many nodes in a level (including None/Null nodes between first and last non-null nodes)
    We can use a heap-like index system to quickly calculate how many nodes are there between two nodes
    Namely, root node has index 1, and for each node with index i, its left child has index 2*i, and its right child has index 2*i+1
    For two nodes on same level with index i and j (j>i), there are (j-i+1) nodes between node i and node j
    (Review heap if this part is confusing)
    
    In order to keep track of indexes of each node, instead of only storing nodes in the queue,
    this time we store a tuple of (node,index) in the queue, so it is very easy to track and insert new nodes and indexes

    Args:
        root (Optional[BinaryTreeNode]) - root node of a binary tree
    Return:
        A list of list, whose elements are the node values on each level, in zigzag order
    """
    def width_of_binaryTree(self, root: Optional[BinaryTreeNode]) -> int:
        if root is None:
            return 0
        # Root node has index 1
        # For a node with index i, its left child has index 2*i, its right child has index 2*i+1
        queue = [(root, 1)]
        max_width = 0
        while queue:
            level_size = len(queue)
            # Width equals to the index of last node subtract the index of the first node plus 1
            # w = queue[-1][1] - queue[0][1] + 1
            level_width = 1 if level_size == 1 else (queue[-1][1] - queue[0][1] + 1)
            # Store the maximum width throught traversal
            max_width = max(max_width, level_width)
            for _ in range(level_size):
                node, num = queue.pop(0)
                if node.left is not None:
                    # For node with index i, its left child has index 2*i
                    queue.append((node.left, 2*num))
                if node.right is not None:
                    # For node with index i, its right child has index 2*i+1
                    queue.append((node.right, 2*num+1))
        return max_width


class MaxDepth:
    """
    Calculate the maximum depth of a given root node of a binary tree (Leetcode 104)

    Depth-First-Search (DFS) of Binary tree, 
    Get the maximum height of left subtree and right subtree, and plus 1 (current level) and return

    Can be used as a template for getting height of a binary tree with DFS

    Args:
        root (Optional[BinaryTreeNode]) - root node of a binary tree
    Return:
        Max depth/height of the given binary tree
    """
    def max_depth(self, root: Optional[BinaryTreeNode]) -> int:
        return 0 if root is None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    

class MinDepth:
    """
    Calculate the minimum depth of a given root node of a binary tree
    Minimum depth is the minimum number of nodes on the shortest path to a leaf node (Leetcode 111)

    Depth-First-Search (DFS) of Binary tree, 
    Get the minimum height of left subtree and right subtree, and plus 1 (current level) and return

    Can be used as a template for binary tree DFS

    Args:
        root (Optional[BinaryTreeNode]) - root node of a binary tree
    Return:
        Min depth of the given binary tree
    """
    def min_depth(self, root: Optional[BinaryTreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        left_height = float('inf')
        right_height = float('inf')
        if root.left is not None:
            left_height = self.minDepth(root.left)
        if root.right is not None:
            right_height = self.minDepth(root.right)
        return min(left_height, right_height) + 1


class PreorderCodec:

    def serialize(self, root: BinaryTreeNode) -> str:
        values = []
        def serialize_recur(node: BinaryTreeNode):
            if node is None:
                values.append('#')
                return
            values.append(str(node.val))
            serialize_recur(node.left)
            serialize_recur(node.right)
        serialize_recur(root)
        return ' '.join(values)

    def deserialize(self, data: str) -> BinaryTreeNode:
        values = iter(data.split())
        def deserialize_recur():
            value = next(values)
            if value == '#':
                return None
            else:
                node = BinaryTreeNode(int(value))
                node.left = deserialize_recur()
                node.right = deserialize_recur()
            return node
        return deserialize_recur()


class LevelOrderCodec:

    def serialize(self, root: BinaryTreeNode) -> str:
        if root is None:
            return ""
        queue = [root]
        values = [str(root.val) if root is not None else '#']
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                    values.append(str(node.left.val))
                else:
                    values.append('#')
                
                if node.right is not None:
                    queue.append(node.right)
                    values.append(str(node.right.val))
                else:
                    values.append('#')
        return ' '.join(values)

    def deserialize(self, data: str) -> BinaryTreeNode:
        if data == '':
            return None
        values = iter(data.split())
        root_value = next(values)
        root = BinaryTreeNode(int(root_value))
        queue = [root]

        while queue:
            node = queue.pop(0)
            left_val = next(values)
            right_val = next(values)
            node.left = BinaryTreeNode(int(left_val)) if left_val != '#' else None
            node.right = BinaryTreeNode(int(right_val)) if right_val != '#' else None
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return root


class ValidSerialization:
    """
    Given a Pre-order serialization, verify if it is a valid serialization without reconstructing the tree (Leetcode 331)

    Args:
        preorder (str) - The Pre-order serialization of a binary tree
    Return:
        A boolean value representing whether is the serialization string is valid or not
    """
    def is_valid_serialization(self, preorder: str) -> bool:
        # Vacancy is how many nodes we can insert so far
        # At the beginning, we can only insert root node, so 1
        vacancy = 1
        for node in preorder.split(','):
            # Every node, None or not None, will take 1 place to insert
            vacancy -= 1
            # If vacancy is less than 0, there is no space to insert new node or None
            if vacancy < 0:
                break
            # If node is None, then it will take 1 slot and create no new slots
            # Because we cannot insert None node after None node
            # If node is not None, then it will take 1 slot and create two new slots
            # Because we can insert None or new nodes on its left and right child
            if node != '#':
                vacancy += 2
        # At the end, a valid tree should have 0 available slots
        # Note that None also takes 1 slot
        return vacancy == 0


class BuildTree:
    """
    Construct a binary tree based on its preorder and inorder traversal (Leetcode 105)

    Use Preorder to find root node of subtree and Inorder to find left and right subtree
     * Preorder - [root] [left_subtree] [right_subtree]
     * Inorder - [left_subtree] [root] [right_subtree]
    The region [left_subtree] always have same number of nodes in Pre-order and In-order, the same as [right-subtree]

    Therefore, no matter it is the whole traversal array, or a part of traversal array standing for a subtree
    The first element of Pre-order is always root node of the subtree
    Then we can find the index of the root node in In-order, and split the traversal array to left subtree and right subtree
    And we can also get the size of left subtree and right subtree from In-order to split Pre-order arrays

    When there is only one value in the range, it is a leaf node, because there is no left and right subtrees on both sides

    Args:
        preorder (List[int]) - List of integers of the pre-order traversal of the binary tree
        inorder (List[int]) - List of integers of the in-order traversal of the binary tree
    Return:
        Root node of the binary tree that generates the pre-order and in-order traversal arrays
    """
    def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[BinaryTreeNode]:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        # Generate an index map to get index of root node in subtree without iteration
        index_map = dict(zip(inorder,range(len(inorder))))
        return self.construct_tree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, index_map)

    def construct_tree(self, preorder: List[int], left1: int, right1: int, inorder: List[int], left2: int, right2: int, index_map: dict) -> BinaryTreeNode:
        if left1 > right1:
            return None
        # The first element of the subarray is always the head of the subtree
        head = BinaryTreeNode(preorder[left1])
        # Base case - head is a leaf node
        if left1 == right1:
            return head
        head_index = index_map[preorder[left1]]
        left_subtree_size = head_index - left2
        # left1...right1 is the range of the subtree in preorder
        # left2...right2 is the range of the subtree in inorder
        # Preorder is root [left_subtree] [right_subtree]
        # Inorder is [left_subtree] root [right_subtree]
        # And they have the same number of nodes in each subtree region
        # We use Preorder to find root node
        # We use Inorder to find left and right subtree
        head.left = self.construct_tree(preorder, left1+1, left1+left_subtree_size, inorder, left2, head_index-1, index_map)
        head.right = self.construct_tree(preorder, left1+left_subtree_size+1, right1, inorder, head_index+1, right2, index_map)
        return head


class CompleteBinaryTree:
    """
    Given the root node of a binary tree, check if it is a complete binary tree (Leetcode 958)

    Variation of BFS of binary tree
    A Tree is not a complete binary tree, if:
    1. It has a node that has right child node and doesn't have left child node
    2. Once it encounters a node that doesn't have both child nodes, all following nodes must be leaf nodes

    Args:
        root (Optional[BinaryTreeNode]) - root node of a binary tree
    Return:
        Whether is the binary tree a complete binary tree
    """
    def is_complete_tree(self, root: Optional[BinaryTreeNode]) -> bool:
        if root is None:
            return True
        queue = [root]
        # Use a boolean flag to record if it encounters a node that doesn't have both child
        must_leaf = False
        while queue:
            # A Tree is not a complete binary tree, if:
            # 1. It has a node that has right child node and doesn't have left child node
            # 2. Once it encounters a node that doesn't have both child nodes, all following nodes must be leaf nodes
            node = queue.pop(0)
            if node.left is None and node.right is not None:
                return False
            elif (node.left is not None or node.right is not None) and must_leaf:
                return False
            elif (node.left is None or node.right is None) and not must_leaf:
                must_leaf = True

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return True


class CompleteBinaryTreeNodeCount:
    """
    Count how many nodes in a given complete binary tree
    The time complexity must be less than O(n) (Leetcode 222)

    For a full binary tree with height h, it has 2^h-1 nodes ... (1)
    In order to utilize feature of complete binary tree as much as possible, we need to traverse as little as possible
    And split complete binary tree into subtrees that are full binary trees, and use the formula (1) to get number of nodes

    First, keep iterating to the left child from root to calculate the height of binary tree
    Then start recursion, and keep iterating the left child of right subtree to get the height of right subtree

    If height of right subtree equals to height, then left subtree is full
    Because Null nodes start on the right subtree
    Use formula to calculate number of nodes on left tree and only traverse right subtree for node number

    If height of right subtree does not equal to height, then right subtree is full
    Because Null nodes start on the left tree, right subtree is a full subtree with height - 1
    Use formula to calculate number of nodes on right tree and only traverse left subtree for node number

    For each subtree, node number = node number of left subtree + 1 (root of subtree) + node number of right subtree

    Args:
        root (Optional[BinaryTreeNode]) - root node of a complete binary tree
    Return:
        Number of nodes in complete binary tree
    """
    # Time complexity O(h+h-1+h-2+h-3+...+1) = O(h^2) = O((log n)^2)
    def count_nodes(self, root: Optional[BinaryTreeNode]) -> int:
        if root is None:
            return 0
        return self.count_complete_subtree(root, 1, self.get_left_most_level(root, 1))
    
    def count_complete_subtree(self, cur: BinaryTreeNode, level: int, height: int) -> int:
        if level == height:
            return 1
        subtree_height = height - level
        right_subtree_depth = self.get_left_most_level(cur.right, level+1)
        if right_subtree_depth == height:
            # If height of right subtree equals to height, then left subtree is full
            # Use formula to calculate number of nodes on left tree and only traverse right subtree for node number
            return ((1 << subtree_height) - 1) + self.count_complete_subtree(cur.right, level+1, height) + 1
        else:
            # If height of right subtree does not equal to height, then right subtree is full
            # Use formula to calculate number of nodes on right tree and only traverse left subtree for node number
            return self.count_complete_subtree(cur.left, level+1, height) + ((1 << (subtree_height-1)) - 1) + 1

    def get_left_most_level(self, cur: BinaryTreeNode, cur_level: int) -> int:
        while cur is not None:
            cur_level += 1
            cur = cur.left
        # Iteration terminted when cur is None, so subtract 1 from current level
        return cur_level - 1
