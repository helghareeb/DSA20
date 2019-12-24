# بسم الله الرحمن الرحيم

class Bag:
    def __init__(self):
        self._items = []
        self._idx = -1

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    # Modify add to accept mulitple values
    # my_bag.add(1,2,3,4,5,6,90)
    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        #self._items.remove(item)
        assert item in self._items
        idx = self._items.index(item)
        return self._items.pop(idx)

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx < len(self) - 1:
            self._idx += 1
            return self._items[self._idx]
        else:
            raise StopIteration
    

    
    

    
