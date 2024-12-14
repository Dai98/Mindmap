import random
from heapq import heappush, heappop


class SetAllHashMap:
    def __init__(self):
        self.map = {}
        self.set_all_val = None
        self.set_all_time = None
        self.timestamp = 0

    """
    Hash map stores a tuple of two elements
    The first element is value
    The second element is the timestamp it got put in
    Put operation will increase timestamp by 1
    """
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            value_arr = self.map[key]
            value_arr[0] = value
            value_arr[1] = self.timestamp
        else:
            self.map[key] = (value, self.timestamp)
        self.timestamp += 1

    def set_all(self, value: int):
        self.set_all_val = value
        self.set_all_time = self.timestamp
        self.timestamp += 1

    """
    Return set all value if this value is added before set all operation (check timestamp)
    Otherwise return the original value corresponding to this key
    """
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        value, timestamp = self.map[key]
        return value if timestamp > self.timestamp else self.set_all_val


class LRUNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRULinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add a new node at the end of LRU linked list
    def add(self, node: 'LRUNode'):
        if node is None:
            return
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    # Remove the current head and use the next node as new head
    def remove_head(self) -> 'LRUNode':
        if self.head is None:
            return
        
        prev_head = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = prev_head.next
            prev_head.next = None
            self.head.prev = None
        return prev_head
    
    # Move the given node to the end of linked list and use it as new tail node
    def move_node_to_tail(self, node: 'LRUNode'):
        if self.tail == node:
            return
        if self.head == node:
            self.head = node.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node


class LRUCache:
    """
    Design a Data Structure that follows Least Recent Used cache (Leetcode 146)

    Use a double linked list to maintain order of updated key-value pairs
    Head node is the least recent used cache, remove head node if size becomes larger than capacity of LRU cache
    Use another hashmap to quickly access to node based on key to avoid iteration on linked list
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.list = LRULinkedList()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        # Once the node is accessed, it is the most recent used node
        # Move it to the end of the linked list
        self.list.move_node_to_tail(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        # If key already exists, update the value
        # Since this node is accessed, move this node to the end of the linked list
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.list.move_node_to_tail(node)
        # If key doesn't exist, create a new node and add it to linked list
        else:
            # If LRU cache is at capacity, remove head node since it represents the least recent used node
            if self.capacity == len(self.map):
                prev_head = self.list.remove_head()
                self.map.pop(prev_head.key)
            # Then create a new node and add it to the end of the LRU linked list
            node = LRUNode(key, value)
            self.map[key] = node
            self.list.add(node)
            

class RandomizedSet:
    """
    Design a Data Structure that supports insert and remove integers like a hash set
    It also supports randomly return an element with equal probability
    All methods should have time complexity O(1)   (Leetcode 380) 

    Use a map to maintain relationship of values and their index in an array
    When remove an element, use the last element to fill in the gap to ensure consecutive index
    (We cannot directly remove elements from an array because either it leaves a gap in index or time complexity of removing is O(n))
    For random access to elements, generate a random number on index of the array
    """
    def __init__(self):
        self.index_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        # If value doesn't exist before, then add it to the end of array
        if val not in self.index_map:
            self.data.append(val)
            self.index_map[val] = len(self.data)-1
            return True
        # If it already exists, don't add it to data
        else:
            return False

    def remove(self, val: int) -> bool:
        # If value doesn't exist in set, don't remove
        if val not in self.index_map:
            return False
        else:
            # If only one element is left, no way to use another element to fill in gap
            # Just clear the list and map since they will be empty after poping
            if len(self.data) == 1:
                self.index_map = {}
                self.data = []
            # If more than one element is left, then we can use another element to fill in the gap
            # To keep a consecutive index for randomly retrieving elements
            else:
                index = self.index_map[val]
                # Use the last element and its index to fill in the gap of removed element
                last_value = self.data[-1]
                self.index_map[last_value] = index
                # Update list and index map
                self.data[index] = last_value
                self.index_map.pop(val)
                self.data.pop()
            return True

    # Return a random element by generating a random number on the range of indexes
    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.index_map)-1)]


class RandomizedCollection:
    """
    Design a Data Structure that supports insert and remove integers, but this time it can save duplicated integers
    It supports randomly return an element, elements with higher frequency should have higher probability
    All methods should have time complexity O(1)   (Leetcode 381) 

    Use a hash map of value and set of indexes of this value to keep track of value and its occurence indexes
    When removing an element, use any of the index of last element to fill in the gap
    The rest of operations are very similar to Randomized Set
    """
    def __init__(self):
        self.index_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        value_presence = val not in self.index_map
        # Put the index of the element in a set
        # Because we can store duplicated values right now
        index_set = self.index_map.get(val, set())
        self.data.append(val)
        index_set.add(len(self.data)-1)
        self.index_map[val] = index_set
        return value_presence

    def remove(self, val: int) -> bool:
        # If value doesn't exist in set, don't remove
        if val not in self.index_map:
            return False
        else:
            index_set = self.index_map[val]
            # Get the index of the gap
            overwrite_index = index_set.pop()
            last_value = self.data[-1]
            # If last element is equal to removed element
            # Use the last element to replace the removed element
            if last_value == val:
                index_set.add(overwrite_index)
                index_set.remove(len(self.data)-1)
            # If last element is another element
            # Get index set of the last element
            else:
                last_value_index_set = self.index_map[last_value]
                # Use the last element to fill in the gap
                # And update index map
                last_value_index_set.add(overwrite_index)
                last_value_index_set.remove(len(self.data)-1)
                self.data[overwrite_index] = last_value
            
            self.data.pop()
            if len(index_set) == 0:
                self.index_map.pop(val)

            return True

    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data)-1)]


class MedianFinder:
    """
    Design a Data Structure that supports add integers to it, and return the median of all added numbers at any time (Leetcode 295)

    Maintain a max heap and a min heap. 
    Store the smaller half of numbers in the max heap, and the larger half of numbers in the min heap
    When asking for median, return the average of two heap roots if two heaps have the same length, 
    or return the heap root of the heap with more elements
    """

    def __init__(self):
        # Python's heapq library only support min heap
        # So all the values stored in max_heap is the reverse of original numbers
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Make the smaller half of numbers in max heap
        # And make the larger half of numbers in min heap
        if len(self.max_heap) == 0 or num <= (-self.max_heap[0]):
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        self.balance()

    def findMedian(self) -> float:
        # If length of two heaps are equal, then median is the average of heap root (Median in an even group of numbers)
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] + (-self.max_heap[0])) / 2
        # If length is not equal, then median is the heap root with larger length (Median in an odd group of numbers)
        else:
            return -self.max_heap[0] if len(self.max_heap) > len(self.min_heap) else self.min_heap[0]

    """
    Make sure that the gap of lengths of max heap and min heap doesn't exceed by 1
    So that each heap always stores half of the integers added
    """
    def balance(self):
        if abs(len(self.max_heap) - len(self.min_heap)) == 2:
            # If the gap is larger than 1
            # Then pop the element from the larger heap and push it to the smaller heap
            if len(self.max_heap) > len(self.min_heap):
                # Python doesn't support max heap, so take reverse for max heap
                element = -heappop(self.max_heap)
                heappush(self.min_heap, element)
            else:
                element = -heappop(self.min_heap)
                heappush(self.max_heap, element)


class FreqStack:
    """
    Design a Data-Structure that implements storing and retrieving frequency of given string key,
    as well as returning key with maximum and minimum frequency (Leetcode 432)

    Use a hash map to track frequency of each element, as well as a variable stored the maximum frequency
    Maintain another hash map with key being frequency and value being a stack of elements with this frequency
    For elements with same frequency, later element will be poped since they are stored in a stack
    """
    def __init__(self):
        self.freq_map = {}
        self.list_map = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.freq_map.get(val, 0) + 1
        # Update frequency and maximum frequency
        self.freq_map[val] = freq
        self.max_freq = max(self.max_freq, freq)
        # Put the element in a stack storing elements with this frequency
        element_list = self.list_map.get(freq, [])
        element_list.append(val)
        self.list_map[freq] = element_list

    def pop(self) -> int:
        # Get the element to pop
        freq_list = self.list_map[self.max_freq]
        # Element pushed later will be poped first
        pop_value = freq_list.pop()
        # Update element frequency
        self.freq_map[pop_value] -= 1
        # Update properties after an element is poped
        if self.freq_map[pop_value] == 0:
            self.freq_map.pop(pop_value)
        if len(freq_list) == 0:
            self.list_map.pop(self.max_freq)
            self.max_freq -= 1
        return pop_value


class BucketNode:
    def __init__(self, freq: int):
        self.keys = set()
        self.freq = freq
        self.prev = None
        self.next = None


class AllOne:
    """
    Design a Data-Structure that implements storing and retrieving frequency of given string keys,
    As well as returning key with maximum and minimum frequency
    All operations should have time complexity O(1) (Leetcode 432)

    Use double linked list to maintain order of frequency because we cannot iterate all keys to get/maintain maximum key
    Nodes are maintained by ordering ascendingly by frequency from head node to tail node
    Node on the right/next of head node is the node with minimum frequency
    Node on the left/prev of tail node is the node with maximum frequency
    """

    def __init__(self):
        self.head = BucketNode(0)
        self.tail = BucketNode(50000)
        # Sentinel buckets to make sure every bucket has prev and last references that are not None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_bucket_map = {}

    """
    Insert a new_bucket after cur_bucket (Insertion in double linked list)
    """
    def _insert(self, cur_bucket: 'BucketNode', new_bucket: 'BucketNode') -> None:
        cur_bucket.next.prev = new_bucket
        new_bucket.next = cur_bucket.next
        cur_bucket.next = new_bucket
        new_bucket.prev = cur_bucket

    """
    Remove cur_bucket from the double linked list
    """
    def _remove(self, cur_bucket: 'BucketNode') -> None:
        cur_bucket.prev.next = cur_bucket.next
        cur_bucket.next.prev = cur_bucket.prev

    def inc(self, key: str) -> None:
        # key doesn't exist before, so it should have frequency 1
        if key not in self.key_bucket_map:
            # Bucket with frequency 1 already exists
            if self.head.next.freq == 1:
                self.key_bucket_map[key] = self.head.next
                self.head.next.keys.add(key)
            # Bucket with frequency 1 doesn't exist
            # Create a new bucket and insert it after head node
            else:
                new_bucket = BucketNode(1)
                new_bucket.keys.add(key)
                self.key_bucket_map[key] = new_bucket
                self._insert(self.head, new_bucket)
        # Keys already exists, then increase frequency by 1
        else:
            bucket = self.key_bucket_map[key]
            # Bucket with 1 more frequency already exists, move the key to the next bucket
            if bucket.next.freq == bucket.freq + 1:
                self.key_bucket_map[key] = bucket.next
                bucket.next.keys.add(key)
            # Bucket with 1 more frequency doesn't exist, create a new bucket and insert it after the current bucket
            else:
                new_bucket = BucketNode(bucket.freq+1)
                new_bucket.keys.add(key)
                self.key_bucket_map[key] = new_bucket
                self._insert(bucket, new_bucket)
            bucket.keys.remove(key)
            if len(bucket.keys) == 0:
                self._remove(bucket)

    def dec(self, key: str) -> None:
        bucket = self.key_bucket_map[key]
        # If current key has frequency 1, then pop this key
        if bucket.freq == 1:
            self.key_bucket_map.pop(key)
        # If current key has frequency more than 1
        # Then reduce its frequency by 1
        else:
            # If bucket with frequency-1 already exists
            # Move the key to the previous bucket
            if bucket.prev.freq == bucket.freq-1:
                self.key_bucket_map[key] = bucket.prev
                bucket.prev.keys.add(key)
            # If bucket with frequency-1 doesn't exist
            # Create a new bucket and insert it after the previous bucket
            else:
                new_bucket = BucketNode(bucket.freq-1)
                new_bucket.keys.add(key)
                self.key_bucket_map[key] = new_bucket
                self._insert(bucket.prev, new_bucket)
        bucket.keys.remove(key)
        # If a bucket doesn't have any keys any more, then remove it from the linked list
        # So that it doesn't provide incorrect keys with minimum and maximum frequency
        if len(bucket.keys) == 0:
            self._remove(bucket)

    def getMaxKey(self) -> str:
        # The previous bucket of tail bucket is the bucket with maximum frequency
        return next(iter(self.tail.prev.keys), "")

    def getMinKey(self) -> str:
        # The next bucket of head bucket is the bucket with minimum frequency
        return next(iter(self.head.next.keys), "")
