# Lab #1
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

def isValid(a_string):
    '''
        >>> isValid('qwertyuiopASDFGHJKLzxcvbnm')
        True
        >>> isValid('hello there, fall is here!')
        False
        >>> isValid('123456yh')
        False
        >>> isValid('POIUYTqwerASDFGHlkjZXCVBMn')
        True
        >>> isValid('POIUYTqwerASDFGHlkjZXCVBnn')
        False
        >>> isValid('12aaaaaaaaaaa6543212345678')
        False
    '''
    # - YOUR CODE STARTS HERE -
    alphabet = []
    char_list = list(a_string)
    
    for char in char_list:
        if char.lower() not in alphabet:
            alphabet.append(char.lower())
    
    if len(alphabet) == 26:
        return True
    else:
        return False

def get_words(filename):
    '''
        Complete the current implementation to work as directed in the handout. No more than 3 lines are required

        .txt file for this doctest is available on Canvas and must be saved in the same directory as your .py file
        >>> get_words('contents.txt')
        ['week', 'bat', 'aquatic', 'eggs', 'threatening', 'crash', 'educated', 'adjoining', 'bent', 'mice', 'belief', 'adjustment', 'blood', 'smooth', 'kaput', 'mountain', 'digestion', 'enchanted', 'wandering', 'fresh']
        >>> len(get_words('contents.txt'))
        20
    '''
    output = []
    with open(filename) as text: # Open, read and close file
        for line in text:        # text contains the entire content of the .txt file
            # - YOUR CODE STARTS HERE -
            output.append(line.strip())
        return output

def get_histogram(words):
    '''
        >>> get_histogram(['hello', 'there', 'spring', 'is', 'here'])
        {5: 2, 6: 1, 2: 1, 4: 1}
        >>> list_of_words = get_words('contents.txt')
        >>> get_histogram(list_of_words)
        {4: 4, 3: 1, 7: 1, 11: 1, 5: 4, 8: 2, 9: 4, 6: 2, 10: 1}
    '''
    # - YOUR CODE STARTS HERE -
    histogram = {}
    get_value = lambda key, dict: dict.get(key)
    
    for word in words:
        word_length = len(word)
        if word_length in histogram.keys():
            histogram.update({word_length: (get_value(word_length, histogram) + 1)})
        else:
            histogram.update({word_length: 1})
    
    return histogram

def removePunctuation(a_string):
    '''
        >>> removePunctuation("Dots...................... many dots..X")
        ('Dots                       many dots  X', {'.': 24})
        >>> data = removePunctuation("I like chocolate cake!!(!! It's the best flavor..;.$ for real")
        >>> data[0]
        'I like chocolate cake      It s the best flavor      for real'
        >>> data[1]
        {'!': 4, '(': 1, "'": 1, '.': 3, ';': 1, '$': 1}
        
    '''
    # - YOUR CODE STARTS HERE -
    char_list = list(a_string)
    char_removed_dict = {}
    
    for pos in range(len(char_list)):
        if not char_list[pos].isalpha() and not char_list[pos] == " ":
            get_value = lambda key, dict: dict.get(key)
            if char_list[pos] in char_removed_dict.keys():
                char_removed_dict.update({char_list[pos]: (get_value(char_list[pos], char_removed_dict) + 1)})
            else:
                char_removed_dict.update({char_list[pos]: 1})
            char_list[pos] = " "
    
    return "".join(char_list), char_removed_dict

if __name__ == "__main__":
    import doctest
    #doctest.run_docstring_examples(isValid, globals(), name='LAB1',verbose=True)   ## Uncomment this line if you want to run doctest by function. Replace get_words with the name of the function you want to run
    doctest.testmod() ## Uncomment this line if you want to run the docstring in all functions
