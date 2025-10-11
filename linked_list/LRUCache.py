from typing import Optional

class Node:
    def __init__(self, key, value, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.capacity = capacity
        self.head = Node("head", "value")
        self.tail = Node("tail", "value")
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node) -> None:
        if self.capacity > 0 and len(self.cache) >= self.capacity:
            lru = self.tail.prev
            self.remove(lru)

        tnext = self.head.next

        self.cache[node.key] = node
        self.head.next = node
        node.prev = self.head
        node.next = tnext
        if tnext:
            tnext.prev = node


    def remove(self, node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[node.key]

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.value = value
            self.insert(node)
        else:
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self.remove(lru)
            new_node = Node(key, value)
            self.insert(new_node)
            self.cache[key] = new_node

if __name__ == "__main__":
    tests = [
        ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    ]

    for i, test in enumerate(tests):
        print(f"Input: {test}")
        # print(f"Output: {solve(test)}")
        print("-" * 20)

        # Create an instance of LRUCache
        lru_cache = LRUCache(2)
        for action, value in zip(test[0], test[1]):
            if action == "LRUCache":
                lru_cache = LRUCache(*value)
                print("null")
            elif action == "put":
                lru_cache.put(*value)
                print("null")
            elif action == "get":
                result = lru_cache.get(*value)
                print(result)
            print("-" * 20)