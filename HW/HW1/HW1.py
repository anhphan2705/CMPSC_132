# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement



def rectangle(perimeter, area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    #- YOUR CODE STARTS HERE
    #Finding 2 variables having sum and product
    length = (perimeter + (perimeter**2 - 16*area)**0.5)/4 #Quaratic formula
    width = area/length
    if length.is_integer() and width.is_integer():
        return int(length)
    else:
        return False
    
def invert(d):
    """
        >>> invert({'one':1, 'two':2,  'three':3, 'four':4})
        {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
        >>> invert({'one':1, 'two':2, 'uno':1, 'dos':2, 'three':3})
        {3: 'three'}
        >>> invert({'123-456-78':'Sara', '987-12-585':'Alex', '258715':'sara', '00000':'Alex'}) 
        {'Sara': '123-456-78', 'sara': '258715'}
    """
    #- YOUR CODE STARTS HERE
    d_items = d.items()
    copy_items = d.copy()
    #Scanning the repeated value using 2D scanning method
    for item_temp in d_items:
        for item in d_items:
            if item_temp[1] == item[1] and item[0] != item_temp[0]:
                copy_items.pop(item_temp[0])
    
    values = copy_items.values()
    keys = copy_items.keys()
                    
    return dict(zip(values, keys))
    

def successors(file):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """

    with open(file) as f: 
        contents = f.read()
        
        contents = contents.replace(",", " , ")
        contents = contents.replace("!", " ! ")
        contents = contents.replace(".", " . ")
    #- YOUR CODE STARTS HERE
    successorss_dict = {}
    word_list = contents.split()
    word_list.insert(0, ".")
    
    for pos_x in range(len(word_list)-1):
        #Creating the initial successor dictionary
        if word_list[pos_x] not in successorss_dict.keys():
            successorss_dict.update({word_list[pos_x]: [word_list[pos_x + 1]]})
        else:
            value = successorss_dict.get(word_list[pos_x])
            if word_list[pos_x+1] not in value:
                value.append(word_list[pos_x+1])
            successorss_dict.update({word_list[pos_x] : value})
            
        for pos_y in range(pos_x+1, len(word_list)):
            #Add more successor to the dictionary if repeated
            if word_list[pos_x] == word_list[pos_y]:
                value = successorss_dict.get(word_list[pos_x])
                if word_list[pos_y+1] not in value:
                    value.append(word_list[pos_y+1])
                successorss_dict.update({word_list[pos_x] : value})
                
    return successorss_dict
            
        
def getPosition(num, digit):
    """
        >>> getPosition(1495, 5)
        1
        >>> getPosition(1495, 1)
        4
        >>> getPosition(1495423, 4)
        3
        >>> getPosition(1495, 7)
        False
    """
    #- YOUR CODE STARTS HERE
    count = 1
    
    while num > 0:
        current_digit = num % 10
        if digit == current_digit:
            return count
        else:
            num = num // 10
            count += 1
    
    return False
            
def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    #- YOUR CODE STARTS HERE
    sequence = [num]
    
    while num > 1:
        if num % 2 == 0:
            num = num//2
            sequence.append(num)
        elif num %2 == 1:
            num = (3*num) + 1
            sequence.append(num)
    
    return sequence
            
def largeFactor(num):
    """
        >>> largeFactor(15)
        5
        >>> largeFactor(80)
        40
        >>> largeFactor(13)
        1
    """
    #- YOUR CODE STARTS HERE
    factors = []
    
    for number_factor in range(1, num+1):
        if num % number_factor == 0 and num != number_factor:
            factors.append(number_factor)
            
    return factors[-1]

if __name__=='__main__':
    import doctest
    doctest.run_docstring_examples(rectangle, globals(), name='HW1',verbose=True) # replace rectangle for the function name you want to test
