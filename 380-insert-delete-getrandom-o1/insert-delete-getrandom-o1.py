import random

class RandomizedSet:
    def __init__(self):
        self.data = []  # List to store the elements
        self.index_map = {}  # Dict to store the index of each element in the list

    def insert(self, val: int) -> bool:
        if val in self.index_map:  # O(1) time complexity for 'in' operation on dict
            return False
        self.data.append(val)  # O(1) time complexity for 'append' operation on list
        self.index_map[val] = len(self.data) - 1  # Update index
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        index = self.index_map[val]
        last = self.data[-1]
        
        # Swap with the last element and pop from list
        self.data[index], self.data[-1] = self.data[-1], self.data[index]
        self.data.pop()  # O(1) time complexity for 'pop' operation on list

        # Update the index map
        del self.index_map[val]  # O(1) time complexity for 'del' operation on dict
        if last != val:
            self.index_map[last] = index  # Update the index of the last element
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)  # O(1) time complexity for 'choice' operation

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()