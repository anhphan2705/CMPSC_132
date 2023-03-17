# the_string = "HeLlo-TheRE-SMILe"
# the_string = the_string.lower()
# temp = the_string.split("-")
# the_string = ",".join(temp)

# print(the_string)


# Recitation Activity 1

def translate(translation, msg):
    """
        >>> translate({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} , '1 UP 2 down left right forward')
        '2 down 2 up right left forward'
        >>> translate({'a':'b', 'candy':'three cookies'}, 'We are in a house of CANDY')
        'we are in b house of three cookies'
    """     
    # -- YOUR CODE STARTS HERE
    msg = msg.lower().split(" ")
    keys = translation.keys()
    
    for index in range(len(msg)):
        if msg[index] in keys:
            msg[index] = translation.get(msg[index])

    return " ".join(msg)

if __name__ == "__main__":
    import doctest
    doctest.testmod()