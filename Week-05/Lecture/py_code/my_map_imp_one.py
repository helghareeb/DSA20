# بسم الله الرحمن الرحيم

from my_map_adt import MyMapADT

class MyMapO(MyMapADT):
    def __init__(self):
        self._keys = []
        self._values = []

        # for iterator
        self._index = -1

    def __len__(self):
        return len(self._keys)

    # check key only
    def __contains__(self, key):
        if key in self._keys:
            return True

    # Ckeck if key exists or not
    # if key does not exist -> add new key
    # if key exists:
    ## get index of key in self._keys
    ## update value of self._values using the same index
    def add(self, key, val):
        if key in self._keys:
            idx = self._keys.index(key)
            self._values[idx] = val
        else:
            self._keys.append(key)
            self._values.append(val)
    
    # remove using key
    def remove(self, key):
        assert key in self._keys
        idx = self._keys.index(key)
        return self._keys.pop(idx), self._values.pop(idx)

    # make my object subscriptable
    def __getitem__(self, key):
        return self._values[self._keys.index(key)]

    def value_of(self, key):
        return self._values[self._keys.index(key)]

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._keys) - 1:
            self._index += 1
            return self._keys[self._index]
        else:
            self._index = -1
            raise StopIteration