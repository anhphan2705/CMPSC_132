# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement


class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__


    def isEmpty(self):
        return True if self.top == None else False

    def __len__(self): 
        # YOUR CODE STARTS HERE
        length = 0
        current = self.top
        #Loop through the stack to count the lenght
        while current is not None:
            current = current.next
            length += 1
        
        return length

    def push(self, value):
        # YOUR CODE STARTS HERE
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            # Setting the next node
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty():
            return None
        else:
            # Removing the top node and link the next one as top
            temp_node = self.top
            self.top = temp_node.next
            return temp_node.value

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.top is None:
            return None
        else:
            return self.top.value
        
#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None


    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None

    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try:
            num = float(txt)
            return True
        except:
            return False
    
    def doubleOp(self, char_list):
        operators = ["+", "-", "*", "/", "^"]
        for i in range(len(char_list)):
            
            if(char_list[i] in operators and (i !=(len(char_list)-1) and char_list[i+1] in operators)):
                return True

        return False

    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing
            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix ('( ( 2 ) )')
            '2.0'
            >>> x._getPostfix ('2 * ( ( 5 + -3 ) ^ 2 + ( 1 + 4 ) )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( ( 2 * ( ( 5 + 3 ) ^ 2 + ( 1 + 4 ) ) ) )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * ( -5 + 3 ) ^ 2 + ( 1 + 4 )')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to post_fix, this cases are not necessary

            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''

        # YOUR CODE STARTS HERE
        post_fixStack = Stack()  # method must use post_fixStack to compute the post_fix expression
        char_list = txt.split()
        operator = [None, "(", ")", "+", "-", "*", "/", "^"]
        post_fix = ""
        char_list.insert(0, "(")
        char_list.append(")")
        
        if self.doubleOp(char_list):
            return None
        
        for char in char_list:
            
            if self._isNumber(char):
                post_fix += str(float(char)) + " "
                
            elif char == "(":
                post_fixStack.push(char)
                
            elif char == ")":
                while post_fixStack.peek() is not "(" and post_fixStack.peek() is not None:
                    post_fix += post_fixStack.pop() + " "
                post_fixStack.pop()
            # Case where char is a operator
            else:
                if char == "":
                    return None
                if char not in operator and not self._isNumber(char):
                    return None
                top_stack = operator.index(post_fixStack.peek())
                while operator.index(char) <= top_stack:
                    post_fix += post_fixStack.pop() + " "
                    top_stack = operator.index(post_fixStack.peek())
                    
                post_fixStack.push(char)

        return post_fix.rstrip()  

    @property
    def calculate(self):
        '''
            calculate must call _getPostfix
            calculate must create and use a Stack to compute the final result as shown in the video lecture
            
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( ( ( 10 - 2 * 3 ) ) )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * ( 3 - 2.45 * ( 4 - 2 ^ 3 ) ) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * ( 4 + 2 * ( 5 - 3 ^ 2 ) + 1 ) + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + ( 3.0 ) * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * ( 4 ) ) * ( 2 / 8 + 2 * ( 3 - 1 / 3 ) ) - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
            >>> x.setExpr('( 3.5 ) ( 15 )') 
            >>> x.calculate
            >>> x.setExpr('3 ( 5 ) - 15 + 85 ( 12 )') 
            >>> x.calculate
            >>> x.setExpr("( -2 / 6 ) + ( 5 ( ( 9.4 ) ) )") 
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None

        calcStack = Stack()   # method must use calcStack to compute the  expression

        # convert an expression from infix to post_fix
        post_fix = self._getPostfix(self.__expr)
        if post_fix is not None:
            post_fix = post_fix.split()
            for pos in range(len(post_fix)):
                if self._isNumber(post_fix[pos]):
                    calcStack.push(post_fix[pos])
                else:
                    # Performing calculation
                    p1 = float(calcStack.pop())
                    p2 = float(calcStack.pop())
                    if post_fix[pos] == '+':
                        calcStack.push(p1 + p2)
                    elif post_fix[pos] == '-':
                        calcStack.push(p2 - p1)
                    elif post_fix[pos] == '/':
                        calcStack.push(p2 / p1)
                    elif post_fix[pos] == '^':
                        calcStack.push(p2 ** p1)
                    elif post_fix[pos] == '*':
                        calcStack.push(p1 * p2)

            return calcStack.top.value
        else:
            return None


#=============================================== Part III ==============================================

class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0, 'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 * ( x1 - 1 );x1 = x2 - x1;return x2 + x1 ^ 3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 * ( x1 - 1 )': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * ( x1 / 2 );x1 = x2 * 7 / x1;return x1 * ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 * ( x1 / 2 )': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}

    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}

    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if word is not None:
            if word[0].isalpha():
                for pos in range(len(word)):
                    if not word[pos].isalnum():
                        return False
                return True
            else:
                return False
       

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 * ( x1 - 1 )')
            '7 * ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        exp = expr.split()
        operators = ["(", ")", "+", "-", "/", "*", "^"]
        new_expr = ""
        isValid = True
        for pos in exp:
            try:
                float(pos)
                new_expr += str(pos)+ " "
            except:
                if pos in operators:
                    new_expr += str(pos) + " "
                elif self._isVariable(pos) and pos in self.states.keys():
                    new_expr += str(self.states[pos]) + " "
                else:
                    isValid = False
                    return None
        if isValid == True:
            return new_expr.strip()

    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest.run_docstring_examples(AdvancedCalculator._replaceVariables, globals(), name='HW3',verbose=True)