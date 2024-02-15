from typing import Any
from abc import abstractmethod, ABC


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


class LinkedList(ABC):
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
            else:
                cur_node = self.head
                # Find the element with given value as targeted element
                while cur_node.next is not None and cur_node.next.value != value:
                    cur_node = cur_node.next
                # If the element with given value can be found, then remove this element
                if cur_node.next is not None and cur_node.next.value == value:
                    cur_node.next = cur_node.next.next
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
            new_head = SingleLinkedNode(value, self.head)
            self.head = new_head
        # In other cases, iterate to the correct index and insert a new node
        else:
            cur_index = 0
            cur_node = self.head
            while cur_index < index-1:
                cur_node = cur_node.next
                cur_index += 1
            new_node = SingleLinkedNode(value, cur_node.next)
            cur_node.next = new_node

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
                self.head = self.head.next
                self.head.prev = self.tail
            elif self.tail.value == value:
                self.head.prev = self.tail.prev
                self.tail = self.tail.prev
                self.tail.next = self.head
            else:
                cur_node = self.head
                while cur_node.next is not None and cur_node.next.value != value:
                    cur_node = cur_node.next
                if cur_node.next is not None and cur_node.next.value == value:
                    cur_node.next = cur_node.next.next
                    cur_node.next.prev = cur_node
                else:
                    return
    
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
            new_head = DoubleLinkedNode(value, self.tail, self.head)
            self.tail.next = new_head
            self.head.prev = new_head
            self.head = new_head
        else:
            cur_index = 0
            cur_node = self.head
            while cur_index < index-1:
                cur_node = cur_node.next
                cur_index += 1
            new_node = DoubleLinkedNode(value, cur_node, cur_node.next)
            cur_node.next = new_node
            cur_node.next.next.prev = new_node

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
        pass

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

    @staticmethod
    def reverse_linkedlist(head: SingleLinkedNode) -> SingleLinkedNode:
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

    @staticmethod
    def merge_two_linkedlists(head1: SingleLinkedNode, head2: SingleLinkedNode) -> SingleLinkedNode:
        if head1 is None or head2 is None:
            return head1 if head1 is not None else head2
        
        head = head1 if head1.value <= head2.value else head2
        cur1 = head.next
        cur2 = head1 if head == head2 else head2
        pre = head

        while cur1 is not None and cur2 is not None:
            if cur1.value <= cur2.value:
                pre.next = cur1
                cur1 = cur1.next
            else:
                pre.next = cur2
                cur2 = cur2.next
            pre = pre.next

        pre.next = cur1 if cur1 is not None else cur2
        return head
    
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

        if carry == 1:
            pre_node.next = SingleLinkedNode(carry, None)
        return result
    
    @staticmethod
    def partition_linkedlist(head: SingleLinkedNode, partition_value: int) -> SingleLinkedNode:
        small_head = None
        small_tail = None
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

        if small_tail is not None:
            small_tail.next = big_head
            return small_head
        else:
            return big_head

if __name__ == "__main__":
    l = SingleLinkedList()
    l.add(2)
    l.add(9)
    l.add(7)
    l.add(4)
    l.add(3)
    l.add(10)
    new_head = LinkedListAlgo.partition_linkedlist(l.head, 5)
    LinkedListAlgo.print_linkedlist_with_head(new_head)
