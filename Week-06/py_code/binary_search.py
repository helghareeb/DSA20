def binary_search( the_values, target ) :
  low = 0
  high = len(the_values) - 1
   
  while low <= high :
    mid = (high + low) // 2
    if the_values[mid] == target :
      return True
    elif target < the_values[mid] :
      high = mid - 1
    else :
      low = mid + 1
   
  return False


if __name__ == '__main__':
    vals = range(0,20,2)
    print(binary_search(vals, 5))
    print(binary_search(vals, 10))
    print(binary_search(vals, 20))
