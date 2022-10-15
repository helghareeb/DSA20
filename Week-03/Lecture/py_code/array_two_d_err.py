# بسم الله الرحمن الرحيم

class MyArrayTD:
    def __init__(self, no_rows, no_cols):
        self.no_rows = no_rows
        self.no_cols = no_cols

        # Given the info that 3 * [] will generate three empty lists
        # We can say that:
        # 2-D Array is a list of lists

        # Create 2-D Array
        # If you try the inner list as empty, 
        # you will get errors later trying to assign values
        self._my_array = no_rows * [ no_cols * [0]]
    
    def num_rows(self):
        return self.no_rows

    def num_cols(self):
        return self.no_cols

    def clear(self, value):
        for row in range(self.no_rows):
            for col in range(self.no_cols):
                self._my_array[row][col] = value

    def set_item(self, row, col, value):
        self._my_array[row][col] = value

    def get_item(self, row, col):
        return self._my_array[row][col]


    def print_array(self):
        for i in range(self.no_rows):
            for j in range(self.no_cols):
                print(f'{self.get_item(i,j)}',end=' ')
            print('\n')

def main():
    arr = MyArrayTD(3,2)
    arr.clear(0)
    print('Initial Array Values')
    arr.print_array()
    print('Set Item: 0,1 to Value: 2')
    arr.set_item(0,1,2)
    arr.print_array()
    

if __name__ == '__main__':
    main()

## Correct Pythonic Way
# # Creates a list containing 5 lists, each of 8 items, all set to 0
# w, h = 8, 5;
# Matrix = [[0 for x in range(w)] for y in range(h)] 