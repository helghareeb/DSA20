# بسم الله الرحمن الرحيم

class Bag:
    def __init__(self):
        self._items = []
        self._current_item = -1

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def add(self, item):
        self._items.append(item)

    # Remove by index
    def remove(self, item):
        assert item in self._items
        idx = self._items.index(item)
        return self._items.pop(idx)

    # Remove by value (Not Recommended)

    # Iterator
    def __iter__(self):
        return self
    
    # Iterator
    def __next__(self):
        if self._current_item < len(self) - 1:
            self._current_item += 1
            return self._items[self._current_item]
        else:
            raise StopIteration

if __name__ == '__main__':
    pass
    # print('I am inside Bag.py')
