#بسم الله الرحمن الرحيم

def bubble_sort( values ):
    n = len( values )
    for i in range( n ) :
        for j in range( n - 1) :
            if values[j] > values[j + 1] :
                values[j], values[j+1] = values[j+1], values[j]
        #print(values)
    return values


if __name__ == '__main__':
    val = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print(bubble_sort(val))
