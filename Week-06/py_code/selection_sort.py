# بسم الله الرحمن الرحيم

def selection_sort( values ):
    n = len( values )
    for i in range( n - 1 ):
        smallNdx = i
        for j in range( i + 1, n ):
            if values[j] < values[smallNdx] :
                smallNdx = j

        if smallNdx != i :
            values[i], values[smallNdx] = values[smallNdx], values[i]
        print(values)
    return values
    
if __name__ == '__main__':
    val = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print(selection_sort(val))
