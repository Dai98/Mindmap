# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
current_folder = Path(__file__).parent
sys.path.append(str(current_folder))

from typing import Any, Optional
from abc import abstractmethod
from base import DataStructureTemplate


class LinkedNode:
    """
        The base class for nodes of Linked List
    """
    def __init__(self, value: Any) -> None:
        self.value = value
    def __str__(self):
        return f"LinkedNode<{str(self.value)}>"


class SingleLinkedNode(LinkedNode):
    """
        Class of node for Single Linked List, inherited from LinkedNode class
        Each node only has reference to the next node
    """
    def __init__(self, value: Any, next: LinkedNode) -> None:
        super().__init__(value)
        self.next = next


class DoubleLinkedNode(LinkedNode):
    """
        Class of node for Double Linked List, inherited from LinkedNode class
        Each node has reference to the previous and next node
    """
    def __init__(self, value: Any, prev: LinkedNode, next: LinkedNode) -> None:
        super().__init__(value)
        self.prev = prev
        self.next = next


class LinkedList(DataStructureTemplate):
    """
        Interface of Linked List, defined basic operation like add, remove and insert an element
    """
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def add(self, value: Any) -> None:
        raise NotImplementedError("linkedlist.py-LinkedList/Abstract method add is not implemented in base class.")
    
    @abstractmethod
    def remove(self, value:Any) -> None:
        raise NotImplementedError("linkedlist.py-LinkedList/Abstract method remove is not implemented in base class.")
    
    @abstractmethod
    def insert(self, index: int, value: Any) -> None:
        raise NotImplementedError("linkedlist.py-LinkedList/Abstract method insert is not implemented in base class.")
    

class SingleLinkedList(LinkedList):
    """
        Implementation of Single Linked List, each node only has reference to the next node
    """
    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    """
        Implementation of adding a new element to the end of a linked list for Single Linked List
        When there are no nodes in the linked list, instantiate head and tail nodes
        When there are nodes in the linked list, directly append a new node to the tail node and update tail node

        Args:
            value (Any) - Value to add
        
        Return:
            None
    """
    def add(self, value: Any) -> None:
        if self.head is None:
            self.head = SingleLinkedNode(value, None)
            self.tail = self.head
        else:
            self.tail.next = SingleLinkedNode(value, None)
            self.tail = self.tail.next
        self.length += 1

    """
        Implementation of removing an element with given value for Single Linked List
        Iterate through linked list and find targeted element. Once found, remove the targeted element

        Args:
            value (Any) - Value stored in removed element. if no elements have this value, then do nothing

        Return:
            None
    """
    def remove(self, value: Any) -> None:
        if self.head is None or value is None:
            return
        else:
            if self.head.value == value:
                self.head = self.head.next
                self.length -= 1
            else:
                cur_node = self.head
                # Find the element with given value as targeted element
                while cur_node.next is not None and cur_node.next.value != value:
                    cur_node = cur_node.next
                # If the element with given value can be found, then remove this element
                if cur_node.next is not None and cur_node.next.value == value:
                    if self.tail == cur_node.next:
                        self.tail = cur_node
                    cur_node.next = cur_node.next.next
                    self.length -= 1
                # If no nodes have this value, then do nothing
                else:
                    return
    
    """
        Implementation of inserting a node at given index for Single Linked List

        Args:
            index (int) - Index to insert a new value
            value (Any) - Value to be inserted into the linked list

        Return:
            None
    """
    def insert(self, index: int, value: Any) -> None:
        # If index is invalid
        if index > self.length or index < 0:
            raise ValueError(f"linkedlist.py-SingleLinkedList/Index out of bound, cannot insert element to index {index}.")
        # If the index is at the end of linked list
        # Then it is the same as adding a new node
        elif index == self.length:
            self.add(value)
        # If given index is 0, then replace the head node
        elif index == 0:
            if self.head is None:
                self.add(value)
            else:
                new_head = SingleLinkedNode(value, self.head)
                self.head = new_head
                self.length += 1
        # In other cases, iterate to the correct index and insert a new node
        else:
            cur_index = 0
            cur_node = self.head
            while cur_index < index-1:
                cur_node = cur_node.next
                cur_index += 1
            new_node = SingleLinkedNode(value, cur_node.next)
            cur_node.next = new_node
            self.length += 1
    """
        Remove all the data and reset the linked list

        Args:
            None
        Return:
            None
    """
    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    """
        A special method overwritten to better display elements in a single linked list
    """
    def __str__(self) -> str:
        node_values = []
        cur_node = self.head
        while cur_node != None:
            node_values.append(str(cur_node.value))
            cur_node = cur_node.next
        return f"[{'->'.join(node_values)}]"


class DoubleLinkedList(LinkedList):
    """
        Implementation of Double Linked List, each node has reference to the previous and next node
        The first and last node is connected, 
            which means that the previous node of the first node is the last node,
            and the next node of the last node is the first node
    """
    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    """
        Implementation of adding a new element to the end of a linked list for Double Linked List
        When there are no nodes in the linked list, instantiate head and tail nodes
        When there are nodes in the linked list, directly append a new node to the tail node and update tail node

        Args:
            value (Any) - Value to add
        
        Return:
            None
    """
    def add(self, value: Any) -> None:
        if self.length == 0:
            self.head = DoubleLinkedNode(value, None, None)
        elif self.length == 1:
            self.tail = DoubleLinkedNode(value, self.head, self.head)
            self.head.prev = self.tail
            self.head.next = self.tail
        else:
            new_node = DoubleLinkedNode(value, self.tail, self.head)
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1
    
    """
        Implementation of removing an element with given value for Double Linked List
        Iterate through linked list and find targeted element. Once found, remove the targeted element

        Args:
            value (Any) - Value stored in removed element. if no elements have this value, then do nothing

        Return:
            None
    """
    def remove(self, value:Any) -> None:
        if self.head is None or value is None:
            return
        else:
            if self.head.value == value:
                if self.length == 1:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                self.length -= 1
            else:
                cur_node = self.head
                while cur_node.next is not None and cur_node.next.value != value:
                    cur_node = cur_node.next
                if cur_node.next is not None and cur_node.next.value == value:
                    if cur_node.next != self.tail:
                        cur_node.next = cur_node.next.next
                        cur_node.next.prev = cur_node
                    else:
                        self.tail = cur_node
                        self.tail.next = self.head
                        self.head.prev = self.tail
                    self.length -= 1

    
    """
        Implementation of inserting a node at given index for Double Linked List

        Args:
            index (int) - Index to insert a new value
            value (Any) - Value to be inserted into the linked list

        Return:
            None
    """
    def insert(self, index: int, value: Any) -> None:
        if index > self.length or index < 0:
            raise ValueError(f"linkedlist.py-DoubleLinkedList/Index out of bound, cannot insert element to index {index}.")
        elif index == self.length:
            self.add(value)
        elif index == 0:
            if self.length == 1:
                new_node = DoubleLinkedNode(value, self.head, self.head)
                self.tail = self.head
                self.head = new_node
                self.head.next = self.tail
                self.head.prev = self.tail
                self.tail.next = self.head
                self.tail.prev = self.head
            else:
                new_node = DoubleLinkedNode(value, self.tail, self.head)
                self.tail.next = new_node
                self.head.prev = new_node
                self.head = new_node
            self.length += 1
        else:
            cur_index = 0
            cur_node = self.head
            while cur_index < index-1:
                cur_node = cur_node.next
                cur_index += 1
            new_node = DoubleLinkedNode(value, cur_node, cur_node.next)
            cur_node.next = new_node
            cur_node.next.next.prev = new_node
            self.length += 1

    """
        Remove all the data and reset the linked list

        Args:
            None
        Return:
            None
    """
    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0

    """
        A special method overwritten to better display elements in a double linked list
    """
    def __str__(self):
        node_values = []
        cur_node = self.head
        while cur_node != self.tail:
            node_values.append(str(cur_node.value))
            cur_node = cur_node.next
        if self.tail is not None:
            node_values.append(str(self.tail.value))
        return f"[{'<->'.join(node_values)}]"


class LinkedListAlgo:
    """
        Implementation of common linked list related problems
        Unless explicitly stated, all linkedlists used in this class are Single Linked List
        All methods are independent of each other, so all methods are static methods
    """
    def __init__(self) -> None:
        raise NotImplementedError("linkedlist.py-LinkedListAlgo/All methods in this class are static. Do not instantiate this class.")
    
    """
        A utility method to print a linked list given the head node of this linked list.
        A string literal will be returned, and the same string literal will also be printed in console.

        Args:
            head (LinkedNode) - The head node of this linked list

        Return:
            A string literal displaying the elements in the linked list

    """
    @staticmethod
    def print_linkedlist_with_head(head: LinkedNode) -> None:
        node_values = []
        cur_node = head
        while cur_node != None:
            node_values.append(str(cur_node.value))
            cur_node = cur_node.next
        linkedlist_str = f"[{'->'.join(node_values)}]"
        print(linkedlist_str)
        return linkedlist_str

    """
        Reverse a linked list given the head of the linked list

        Example 1:
            Input: 1->2->3->null          Output: 3->2->1->null

        Example 2:
            Input: null                   Output: null
        
        Problem link: https://leetcode.com/problems/reverse-linked-list/description/

        Args:
            head (SingleLinkedNode) - The head node of a single linked list to reverse
        
        Return:
            The new head of the reversed single linked list
    """
    @staticmethod
    def reverse_linkedlist(head: SingleLinkedNode) -> SingleLinkedNode:
        # It is impossible to reverse the linked list with solely current node
        # So we need reference to the previous and next node of the current node to change reference
        pre = None
        next = None
        while head is not None:
            # Get next before we reverse the linked node
            # Because after reversion we will not be able to get the next node
            next = head.next
            # Conduct Reversion
            head.next = pre
            # Update pre and head
            pre = head
            head = next
        # Return pre because head is None right now, and pre is the last node in the linkedlist
        return pre

    """
        Merge two sorted linked list with their heads

        Example 1:
            Input: 1->3->5, 2->4->6       Output: 1->2->3->4->5->6

        Example 2:
            Input: 1->2->4, 1->3->4       Output: 1->1->2->3->4->4
        
        Problem link: https://leetcode.com/problems/merge-two-sorted-lists/description/

        Args:
            head1 (SingleLinkedNode) - The head node of the first single linked list to merge
            head2 (SingleLinkedNode) - The head node of the second single linked list to merge
        
        Return:
            The new head of the merged single linked list
    """
    @staticmethod
    def merge_two_linkedlists(head1: SingleLinkedNode, head2: SingleLinkedNode) -> SingleLinkedNode:
        # If one of the linked list is None
        if head1 is None or head2 is None:
            return head1 if head1 is not None else head2
        
        # Use whichever is smaller as new head
        head = head1 if head1.value <= head2.value else head2
        # Since head already stores the first value of one linked list, 
        # we can use next node as the traverse node
        cur1 = head.next
        cur2 = head1 if head == head2 else head2
        pre = head
        
        # Find the smaller node to append to the new head node
        while cur1 is not None and cur2 is not None:
            if cur1.value <= cur2.value:
                pre.next = cur1
                cur1 = cur1.next
            else:
                pre.next = cur2
                cur2 = cur2.next
            pre = pre.next

        # If there are any left linked list, 
        # then it means that all of its value is larger than the tail of the other linked list
        # Directly append the rest to the tail of merged linked list
        pre.next = cur1 if cur1 is not None else cur2
        return head
    
    """
        Simulate addition with two linked list
        Each number are stored in a node in linked list, and each digits are stored in reverse order
        And the result should also be returned in reverse order
        e.g. 9768 will be 8->6->7->9

        There will be no padding 0s at the beginning of the numbers

        Example 1:
            Input: 8->6->7->9, 2->3->9          Output: 0->0->7->0->1

        Example 2:
            Input: 2,8                          Output: 0->1

        Args:
            head1 (SingleLinkedNode) - The head node of the first number linked list for addition
            head2 (SingleLinkedNode) - The head node of the second number linked list for addition

        Return:
            A SingleLinkedNode as the head node of the result
    
    """
    @staticmethod
    def add_two_linkedlists(head1: SingleLinkedNode, head2: SingleLinkedNode) -> SingleLinkedNode:
        result = None
        pre_node = None
        carry = 0
        while head1 is not None or head2 is not None:
            value = (head1.value if head1 is not None else 0) + (head2.value if head2 is not None else 0) + carry
            carry = value // 10
            value = value % 10

            if pre_node is None:
                result = SingleLinkedNode(value, None)
                pre_node = result
            else:
                pre_node.next = SingleLinkedNode(value, None)
                pre_node = pre_node.next

            head1 = head1.next if head1 is not None else None
            head2 = head2.next if head2 is not None else None

        # Check if an extra digit 1 should be append because of carry
        if carry == 1:
            pre_node.next = SingleLinkedNode(carry, None)
        return result
    
    """
        Partition a linked list with a given integer
        Put all the values less than the integer on the left with same order,
        and put all the values greater or equal than the integer on the right with same order

        Example 1: 
            Input: 1->4->3->2->5->2, 3     Output: 1->2->2->4->3->5

        Example 2:
            Input:

        Problem Link: https://leetcode.com/problems/partition-list/description/

        Args:
            head (SingleLinkedNode) - The head node of the linked list to be partitioned
            partition_value (int) - The given integer used to partition the linked list

        Return:
            A SingleLinkedNode as the head node of the partitioned linked list
    
    """
    @staticmethod
    def partition_linkedlist(head: SingleLinkedNode, partition_value: int) -> SingleLinkedNode:
        # Create two new linked list and concat them after partition them
        # Small head and tail defines a linked list that stores values less than partition_value
        small_head = None
        small_tail = None
        # Big head and tail defines a linked list that stores values greater or equal than partition_value
        big_head = None
        big_tail = None

        while head is not None:
            if head.value < partition_value:
                if small_head is None:
                    small_head = SingleLinkedNode(head.value, None)
                    small_tail = small_head
                else:
                    small_tail.next = SingleLinkedNode(head.value, None)
                    small_tail = small_tail.next
            else:
                if big_head is None:
                    big_head = SingleLinkedNode(head.value, None)
                    big_tail = big_head
                else:
                    big_tail.next = SingleLinkedNode(head.value, None)
                    big_tail = big_tail.next
            head = head.next

        # If there are any nodes on small linked list, then concat the small tail with big head
        if small_tail is not None:
            small_tail.next = big_head
            return small_head
        else:
            return big_head
    
    """
    Given the head nodes of two singly linked lists who don't contain cycles,
    if they intersects at a certain node, return the first node they encounter (Leetcode 160)
    
    If the last nodes of two linked lists have the same memory address, they must intersect at a certain node
    Get the length difference n of two linked lists, let the longer one move n steps first, then compare node one by one

    Args:
        headA (SingleLinkedNode) - The head node of the first linked list to find intersection
        headB (SingleLinkedNode) - The head node of the second linked list to find intersection
    Return:
        The node of first intersection, or None if two linked lists are not intersected
    """
    @staticmethod
    def get_intersection_node(headA: SingleLinkedNode, headB: SingleLinkedNode) -> Optional[SingleLinkedNode]:
        length_A = 0
        length_B = 0
        cur_A = headA
        cur_B = headB

        while cur_A.next is not None:
            cur_A = cur_A.next
            length_A += 1

        while cur_B.next is not None:
            cur_B = cur_B.next
            length_B += 1

        # If the last nodes of two linked lists have the same memory address, they must intersect at a certain node
        if cur_A != cur_B:
            return None
        else:
            long_head = headA if length_A >= length_B else headB
            short_head = headA if long_head == headB else headB
            extra_steps = abs(length_A - length_B)
            current_steps = 0

            # Get the length difference n of two linked lists, let the longer one move n steps first, then compare node one by one
            while current_steps < extra_steps and long_head.next is not None:
                long_head = long_head.next
                current_steps += 1

            while long_head != short_head and long_head is not None and short_head is not None:
                long_head = long_head.next
                short_head = short_head.next

            return long_head


class ReverseKGroup:
    """
    Given the head of a linked list, reverse k nodes at a time, and return the modified list (Leetcode 25)

    Separate the problems into multiple smaller problems
    - Get the node after k nodes
    - Reverse linked list within a given range
    - How to handle new head, as well as the head and tail of each group after reversing, how to connect each group

    Handle the first group separately because the tail of the first group will be the new head
    Overall logic is not hard, implementation is the harder part
    """
    def reverse_k_group(self, head: Optional[SingleLinkedNode], k: int) -> Optional[SingleLinkedNode]:
        start = head
        end = self.get_next_k_node(start, k)
        if end is None:
            return head

        # The end node of first group will become new head
        head = end
        self.reverse(start, end)
        # After reversing, the start of last group becomes the end of last group
        last_end = start

        while last_end.next is not None:
            start = last_end.next
            end = self.get_next_k_node(start, k)
            if end is None:
                return head
            self.reverse(start, end)
            last_end.next = end # end will become the first node of this group
            last_end = start # start will become the last node of this group
        return head

    # Get the k-th node starting from start node (including start node)
    def get_next_k_node(self, node: SingleLinkedNode, k: int) -> bool:
        k -= 1
        while k > 0 and node is not None:
            node = node.next
            k -= 1
        return node

    # s -> a -> b -> c -> e -> n
    # Will become e -> c -> b -> a -> s -> n
    def reverse(self, start: SingleLinkedNode, end: SingleLinkedNode):
        end = end.next  # Get reference to n
        pre, next, cur = None, None, start

        while cur != end:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        start.next = end  # Make s point to n


class RandomNode:
    def __init__(self, x: int, next: 'RandomNode' = None, random: 'RandomNode' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class CopyRandomList:
    """
    For each node of a linked list, it has an extra pointer pointing to a random node or None
    Deep copy this linked list (Leetcode 138)

    Insert the copied nodes after their original nodes, 
    so that we know where to find the copied nodes when we assign random pointers
    At last, separate the copied linked list and original linked list 

    Args:
        head (Optional[RandomNode]) - The head of the linked list to copy
    Return:
        Head node of the copied linked list
    """
    def copy_random_list(self, head: 'Optional[RandomNode]') -> 'Optional[RandomNode]':
        if head is None:
            return None

        cur = head
        next = None
        # Insert copy nodes next to its original node
        # 1 -> 2 -> 3 -> None => 1 -> 1' -> 2 -> 2' -> 3 -> 3' -> None
        while cur is not None:
            next = cur.next
            cur.next = RandomNode(cur.val)
            cur.next.next = next
            cur = next

        # Go back to head and copy random pointers based on the fact that
        # Copied nodes are the next node of its origin
        cur = head
        copy = None
        while cur is not None:
            next = cur.next.next
            copy = cur.next
            copy.random = cur.random.next if cur.random is not None else None
            cur = next

        # Separate the original linked list and copied linked list
        copy_head = head.next
        cur = head
        while cur is not None:
            next = cur.next.next
            copy = cur.next
            cur.next = next
            copy.next = next.next if next is not None else None
            cur = next
        return copy_head


class PalindromeLinkedList:
    """
    Given the head of a singly linked list, return true if it is a palindrome or false otherwise (Leetcode 234)
    
    Use slow-fast pointers to find middle point of the linked list,
    and reverse the second half of the linked list to check if it is palindrome
    
    Args:
        head (Optional[SingleLinkedNode]) - The head of the linked list to check palindrome
    Return:
        True if linked list is a palindrome, False otherwise
    """
    def is_palindrome(self, head: Optional[SingleLinkedNode]) -> bool:
        if head is None or head.next is None:
            return True

        # Use slow-fast pointers to find mid point of the linked list
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Mid point is slow, reverse linked list starting from slow
        pre = slow
        cur = pre.next
        next = None
        # Mid node points to None to avoid infinite loop
        pre.next = None
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        # The last node becomes pre, the first node is head
        left = head
        right = pre
        result = True
        # Compare from both side if linked list is palindrome
        while left is not None and right is not None:
            if left.val != right.val:
                result = False
                break
            left = left.next
            right = right.next

        # Optional, restore linked list back to normal
        cur = pre.next
        pre.next = None
        next = None
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return result


class DetectCycle:
    """
    Given the head of a linked list, return the node where the cycle begins
    If there is no cycle, return null (Leetcode 142)

    Use slow and fast pointer, slow pointer moves by 1 step each iteration, and fast pointer moves 2 steps each iteration
    If fast pointer reaches None during iteration, there is no circle

    If there exists circle, then slow and fast pointer will eventually meet (Reached on node with same memory address)

    Denote that X = distance before circle, Y = distance from the start of the circle to where slow and fast meet
        C = length of the circle, N = number of circles it takes for slow and fast to meet

    Then,
        Distance traveled by slow = X + Y, Distance travenled by fast = 2(X + Y)
    We can have
        2(X + Y) - (X + Y) = N * C
        X + Y = N * C

    Therefore, let slow continues to move 1 step from Y, and fast goes back to the start of linked list and moves 1 step each time

    When slow moves by X steps, it will reach the first node of circle, and so is fast pointer

    So here concludes the step:
        - Define two pointers, slow and fast (slow moves 1 step and fast moves 2 steps each time)
        - Keeps iteration until fast reaches None or fast meets slow
        - Put fast back to start and leave slow at the same node, move both pointers 1 step each time until they meet again
        - The node they meet is the first node of the circle
    
    Args:
        head (Optional[SingleLinkedNode]) - The head of the given linked list
    Return:
        The entering node of the circle, or None if no circle exists in the linked list
    """
    def detect_cycle(self, head: Optional[SingleLinkedNode]) -> Optional[SingleLinkedNode]:
        # None node or 1 node doesn't have circle, 2-node might not have circles
        if head is None or head.next is None or head.next.next is None:
            return None
        
        # Make them start from different nodes to avoid same memory address
        slow = head.next
        fast = head.next.next
        while slow != fast and fast is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else None

        # No circle
        if fast is None:
            return None

        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
    

class LinkedListMergeSort:
    def __init__(self):
        self.start = None
        self.end = None

    """
    Given a linked list head node, sort the linked list ascendingly (Leetcode 148)

    An implementation of merge sort on linked list, use loops instead of recursion for true O(1) space complexity
    The logic is not hard if you are familiar with merge sort, the code is the harder part

    Args:
        head (Optional[SingleLinkedNode]) - The head of the linked list to sort
    Return:
        The new head of the sorted linked list
    """
    def sort_list(self, head: Optional[SingleLinkedNode]) -> Optional[SingleLinkedNode]:
        # Get the length of linked list first to control step size
        n = 0
        cur = head
        while cur is not None:
            n += 1
            cur = cur.next
        # l1...r1 is the left piece of merge sort
        # l2...r2 is the right piece of merge sort

        step = 1
        while step < n:
            # Do the first group separately because head of linked list will change
            l1 = head
            r1 = self.find_node_after_step(l1, step)
            l2 = r1.next
            r2 = self.find_node_after_step(l2, step)
            next = r2.next
            r1.next = None
            r2.next = None
            self.merge(l1, r1, l2, r2)
            head = self.start
            last_group_end = self.end

            while next is not None:
                l1 = next
                r1 = self.find_node_after_step(l1, step)
                l2 = r1.next
                # In case the remaining part is not long enough for the second piece
                if l2 is None:
                    last_group_end.next = l1
                    break
                r2 = self.find_node_after_step(l2, step)
                next = r2.next
                r1.next = None
                r2.next = None
                self.merge(l1, r1, l2, r2)
                last_group_end.next = self.start
                last_group_end = self.end
            step *= 2
        return head

    # Find the node after k nodes of given node (including given node)
    # If the remaining list doesn't have k nodes, then return the last node
    def find_node_after_step(self, node: SingleLinkedNode, k: int) -> SingleLinkedNode:
        k -= 1
        while node.next is not None and k != 0:
            node = node.next
            k -= 1
        return node

    # Merge two pieces of linked list, namely l1...r1, l2...r2
    def merge(self, l1: SingleLinkedNode, r1: SingleLinkedNode, l2: SingleLinkedNode, r2: SingleLinkedNode) -> None:
        # pre is the pointer to the last node of current node, to adjust next pointer
        pre = None
        # Initialize the first node
        if l1.val <= l2.val:
            self.start = l1
            pre = l1
            l1 = l1.next
        else:
            self.start = l2
            pre = l2
            l2 = l2.next
        
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                pre.next = l1
                pre = l1
                l1 = l1.next
            else:
                pre.next = l2
                pre = l2
                l2 = l2.next
        # In case one of the pieces has remaining nodes
        if l1 is not None:
            pre.next = l1
            self.end = r1
        else:
            pre.next = l2
            self.end = r2