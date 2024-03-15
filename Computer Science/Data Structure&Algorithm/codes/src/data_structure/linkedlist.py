# Add current folder to enable importing
import sys
from pathlib import Path
src_folder = Path(__file__).parent.parent.parent
current_folder = Path(__file__).parent
sys.path.append(str(current_folder))

from typing import Any
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
