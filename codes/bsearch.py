"""
file: bsearch.py
purpose: Lecture demonstrates the recursive binary search algorithm.
author: RIT CS Dept.
"""

def binary_search( data, target, start, end ):
    """
    binary_search : List(Orderable) Orderable NatNum NatNum -> NatNum or NoneType
    Perform a binary search for a target value between start and end indices.
    Parameters:
        data - a list of sorted data
        target - the target value to search for
        start - the starting index in data that is part of this search
        end - the ending index in data that is part of this search
    Returns:
        index of target in data, if present; otherwise None.
    """
    
    # base condition - terminate when start passes end index
    if start > end:
        return None
    
    # find the middle value between start and end indices
    mid_index = ( start + end ) // 2
    mid_value = data[mid_index]
    
    # debug statement prints the data list 
    print( "Searching for", target, ":", data[start:mid_index], 
            "*" + str( mid_value ) + "*", 
            data[mid_index+1:end+1] )
    
    if target == mid_value:
        return mid_index
    elif target < mid_value:
        return binary_search( data, target, start, mid_index-1 )
    else:
        return binary_search( data, target, mid_index+1, end )
        
def get_index( data, target ):
    """
    get_index : List(Orderable) Orderable -> NatNum or NoneType
    get_index returns the index of target in data or None if not target found.
    Parameters:
        data - a list of sorted data
        target - the target value to search for
    Returns:
        The index of the target element in data, if it is present,
        otherwise None.
    """
    
    # search for the target across all elements in data
    return binary_search( data, target, 0, len( data ) - 1 )

def main():
    """
    main : Void -> None
    main creates an ordered list of Integers based on user parameters and
    allows the user to 'binary search' for values.
    """
    
    print( "Step 1 - Create your sorted data..." )
    start = int( input( "Start: " ) )
    stop = int( input( "Stop: " ) )
    step = int( input( "Step: " ) )
   
    data = []
    for loop in range ( start, stop, step ):
            data += [loop]

    print( "\nData: ", data )
    print( "Number of elements: ", len( data ) )
    
    print( "\nStep 2 - Enter target value to search for..." )
    target = int( input( "Target: " ) )
    
    print( "\nStep 3 - Get index of target value in data (None if doesn't exist)..." )
    index = get_index( data, target )
    print()
    if index != None:
        print( target, "found at index", index )
    else:
        print( target, "not found" )
    
# # run program

if __name__ == "__main__":
    main()