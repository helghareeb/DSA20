# بسم الله الرحمن الرحيم

def insertion_sort( values ):
    n = len( values )
    for i in range( 1, n ) :
        value = values[i]
        pos = i
        while pos > 0 and value < values[pos - 1] :
            values[pos] = values[pos - 1]
            pos -= 1

        values[pos] = value

    return values

if __name__ == '__main__':
    val = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print(insertion_sort(val))
