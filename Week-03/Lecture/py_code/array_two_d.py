# بسم الله الرحمن الرحيم

from my_array import MyArray

class MyArrayTD:
    def __init__(self, no_rows, no_cols):
        
        # Optional but will make code easier later
        # self.no_rows = no_rows
        # self.no_cols = no_cols

        # Create Outer Array
        self._rows = MyArray(no_rows)

        # Create Internal Arrays for each Outer Array
        for row in range(no_rows):
            self._rows[row] = MyArray(no_cols)

    def num_rows(self):
        # return self.num_rows
        return len(self._rows)

    def num_cols(self):
        # return self.num_cols
        return len(self._rows[0])

    def clear(self, value):
        for row in range(self.num_rows()):
            # this clear implementation inside my_array
            row.clear(value)

    # Make array subscriptable
    def __getitem__(self, idx_tuple):
        assert len(idx_tuple) == 2, 'Invalid number'
        row = idx_tuple[0]
        col = idx_tuple[1]
        assert row >= 0 and row <= self.num_rows() and \
            col >= 0 and col <= self.num_cols(), \
                'Array subscript out of range'
        the_one_d_arr = self._rows[row]
        return the_one_d_arr[col]

    # Make array subscriptable
    def __setitem__(self, idx_tuple, value):
        assert len(idx_tuple) == 2, 'Invalid number'
        row = idx_tuple[0]
        col = idx_tuple[1]
        assert row >= 0 and row <= self.num_rows() and \
            col >= 0 and col <= self.num_cols(), \
                'Array subscript out of range'
        the_one_d_arr = self._rows[row]
        the_one_d_arr[col] = value
    