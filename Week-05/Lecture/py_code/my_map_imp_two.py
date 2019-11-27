# بسم الله الرحمن الرحيم

from my_map_adt import MyMapADT

class MyMap(MyMapADT):
    def __init__(self):
        self._inner = []

        # for iterator
        self._index = -1

    def __len__(self):
        return len(self._inner)

    def __contains__(self, key):
        for it in self._inner:
            if it[0] == key:
                return True
        return False

    # Ckeck if key exists or not
    # if key does not exist -> add new key
    # if key exists:
    ## get index of key in self._keys
    ## update value of self._values using the same index
    def add(self, key, val):
        for it in self._inner:
            if it[0] == key:
                it[1] == val
        else:
            self._inner.append([key, val])

    def remove(self, key):
        assert self.__contains__(key)
        for idx, it in enumerate(self._inner):
            if it[0] == key:
                self._inner[idx] = None

    def value_of(self, key):
        assert self.__contains__(key)
        for it in self._inner:
            if it[0] == key:
                return it[1]

    def __getitem__(self, key):
        for it in self._inner:
            if it[0] == key:
                return it[1]

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self) - 1:
            self._index += 1
            return self._inner[self._index][0]
        else:
            self._index = -1
            raise StopIteration