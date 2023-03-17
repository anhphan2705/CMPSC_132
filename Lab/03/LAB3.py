# LAB3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# All functions should NOT contain any for/while loops or global variables. Use recursion, otherwise no credit will be given

def get_count(aList, item):
    '''
        >>> get_count([1,4,3.5,'1',3.5, 9, 1, 4, 2], 1)
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 3.5)  
        2
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 9)   
        1
        >>> get_count([1,4,3.5,'1',3.5, 9, 4, 2], 'a') 
        0
    '''
    ## YOUR CODE STARTS HERE
    #Check if item is a list
    if not isinstance(item, list):
        data = [item, 0]
    else:
        data = item
    #Using the item to save [number, count]
    if data[0] in aList and aList is not []:
        aList.remove(data[0])
        data[1] +=1
        return get_count(aList, data)
    else:
        return data[1]
        
def replace(numList, old, new):
    '''
        >>> input_list = [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace(input_list, 1, 99.9)
        [99.9, 7, 5.6, 3, 2, 4, 99.9, 9]
        >>> input_list
        [1, 7, 5.6, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 5.6, 777) 
        [1, 7, 777, 3, 2, 4, 1, 9]
        >>> replace([1,7, 5.6, 3, 2, 4, 1, 9], 8, 99)    
        [1, 7, 5.6, 3, 2, 4, 1, 9]
    '''
    ## YOUR CODE STARTS HERE
    numList_copy = numList.copy()  
    # Keep changing until the old number is completely removed
    if old in numList_copy:
        numList_copy[numList_copy.index(old)] = new
        return replace(numList_copy, old, new)
    else:
        return numList_copy


def cut(aList):
    '''
        >>> cut([7, 4, 0])
        [7, 4, 0]
        >>> myList=[7, 4, -2, 1, 9]
        >>> cut(myList)   # Found(-2) Delete -2 and 1
        [7, 4, 9]
        >>> myList
        [7, 4, -2, 1, 9]
        >>> cut([-4, -7, -2, 1, 9]) # Found(-4) Delete -4, -7, -2 and 1
        [9]
        >>> cut([-3, -4, 5, -4, 1])  # Found(-3) Delete -3, -4 and 5. Found(-4) Delete -4 and 1
        []
        >>> cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]) # Found(-1) Delete -1. Found(-3) Delete -3, 1 and 8. Found(-2) Delete -2 and 0
        [5, 7, 6, 785, 5, 0, 42]
    '''
    ## YOUR CODE STARTS HERE
    #Check if it's empty
    if len(aList) == 0:
        return aList
    #If value is positive, keep the value and repeat from the next value
    elif aList[0] >= 0:
        return [aList[0]] + cut(aList[1:])
    #If negative 
    else:
        return cut(aList[abs(aList[0]):])

def neighbor(n):
    '''
        >>> neighbor(24680)
        24680
        >>> neighbor(2222466666678)
        24678
        >>> neighbor(0)
        0
        >>> neighbor(22224666666782)
        246782
        >>> neighbor(2222466666625)
        24625
    '''
    ## YOUR CODE STARTS HERE
    if n == 0:
        return n
    #Check if the last number equals to the previous number
    elif n % 10 is not (n // 10) % 10:
        return neighbor(n//10)* 10 + n % 10
    else:
        return neighbor(n//10)
    
if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(cut, globals(), name='LAB2',verbose=True) # replace Fibonacci for the class name you want to test