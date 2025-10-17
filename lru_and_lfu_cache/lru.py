# ===== LRU Cache Implementation =====
class LRUCache:
    # Inner class for doubly linked list nodes
    class ListNode:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}  # Dictionary to map key -> ListNode for O(1) access

        # Dummy head and tail nodes to simplify insertion/deletion
        self.head = self.ListNode(-1, -1)
        self.tail = self.ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper: remove a node from the linked list
    def deletefromBack(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    # Helper: insert a node right after the head (most recently used)
    def insertAfterHead(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    # Get the value of a key
    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1  # Key not present

        node = self.mp[key]
        # Move the accessed node to the head (mark as most recently used)
        self.deletefromBack(node)
        self.insertAfterHead(node)
        return node.val

    # Put a key-value pair in the cache
    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            # If key exists, update value and move to head
            node = self.mp[key]
            node.val = value
            self.deletefromBack(node)
            self.insertAfterHead(node)
        else:
            # If cache is full, remove least recently used node (tail.prev)
            if len(self.mp) == self.capacity:
                last_node = self.tail.prev
                self.deletefromBack(last_node)
                del self.mp[last_node.key]

            # Insert new node at head
            new_node = self.ListNode(key, value)
            self.mp[key] = new_node
            self.insertAfterHead(new_node)

# ===== Driver Code (Simulating operations) =====
operations = ["LRUCache","put","put","get","put","get","put","get","get","get"]
values = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

lru = None
results = []

# Execute operations sequentially
for op, val in zip(operations, values):
    if op == "LRUCache":
        # Initialize LRU Cache with given capacity
        lru = LRUCache(val[0])
        results.append(None)
    elif op == "put":
        # Insert key-value pair
        lru.put(val[0], val[1])
        results.append(None)
    elif op == "get":
        # Access value by key
        res = lru.get(val[0])
        results.append(res)

# Print results (None for 'put', value for 'get')
print("Results of operations:", results)
