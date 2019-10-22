# بسم الله الرحمن الرحيم

class MySet:
    def __init__(self, list=None):
        # Later, we will need the following functionality
        if list:
            self._items = list
        else:
            self._items = []
        self.idx = -1

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def add(self, item):
        if not item in self._items:
            self._items.append(item)

    def remove(self, item):
        assert item in self._items
        # Again, the same two options: index, value
        # self._items.remove(item)
        idx = self._items.index(item)
        return self._items.pop(idx)

    def __eq__(self, set_b):
        return self.is_subset_of(set_b) and set_b.is_subset_of(self)

    def is_subset_of(self, set_b):
        for item in self._items:
            # if item not in set_b:
            #     return False
            if item in set_b:
                pass
            else:
                return False
        return True
    
    # def union(self, set_b):
    def __add__(self, set_b):
        # _union_list = self._items[]
        _union_list = self._items[:]
        for item in set_b:
            if item not in self._items:
                _union_list.append(item)
        # We need extra funtionality to return Set, not a list
        return MySet(_union_list)

    def intersect(self, set_b):
        _intersect_list = []
        for item in self._items:
            if item in set_b:
                _intersect_list.append(item)
        return MySet(_intersect_list)

    # def difference(self, set_b)
    def __sub__(self, set_b):
        _diff_list = []
        for item in self._items:
            if item not in set_b:
                _diff_list.append(item)
        for item in set_b:
            if item not in self._items and item not in _diff_list:
                _diff_list.append(item)
        return MySet(_diff_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self._items) - 1:
            self.idx += 1
            return self._items[self.idx]
        else:
            raise StopIteration

    def __repr__(self):
        return str(self._items)
