class Complex:
    """ Complex number of the form a + bi, where a and b are real numbers, and i is an indeterminate satisfying i2 = −1 """

    def __init__(self,r,i):
        self._real = r
        self._imag = i
        
    def __str__(self):
        """Display complex number"""
        if self._imag>=0:
           return f"{self._real} + {self._imag}i"
        else:
           return f"{self._real} - {abs(self._imag)}i"

    __repr__ = __str__
    
    def conjugate(self):
        """Returns a Complex object that represents the complex conjugate"""
        return Complex(self._real, -self._imag)
    
    def __mul__(self, other):
        """Multiply a Complex number"""
        #(x+yi) * real = (x*real) + (y*real)i
        if isinstance(other, Complex):
            #(x+yi) * (u+vi) = (xu-yv) + (xv+yu)i
            a = self._real * other._real - self._imag * other._imag
            b = self._real * other._imag + self._imag * other._real
            ans = Complex(a, b)
        else:
            #(x+yi) * real = (x*real) + (y*real)i
            a = self._real * other
            b = self._imag * other
            ans = Complex(a, b)
        return ans
    
    def __rmul__(self, other):
        """Multiply a real and Complex number"""
        if isinstance(other, Complex):
            #(x+yi) * (u+vi) = (xu-yv) + (xv+yu)i
            a = self._real * other._real - self._imag * other._imag
            b = self._real * other._imag + self._imag * other._real
            ans = Complex(a, b)
        else:
            #(x+yi) * real = (x*real) + (y*real)i
            a = self._real * other
            b = self._imag * other
            ans = Complex(a, b)
        return ans


class Real(Complex):
    ''' Returns True if other is a Real object that has the same value or if other is
    a Complex object with _imag=0 and same value for _real, False otherwise

    >>> x = Real(3) 
    >>> int(x) * [1,2,3] 
    [1, 2, 3, 1, 2, 3, 1, 2, 3]
    >>> y = int(x) 
    >>> y
    3
    >>> isinstance(y, int) 
    True
    >>> isinstance(y, Real) 
    False
    >>> z = float(x)        
    >>> z                   
    3.0
    >>> isinstance(z, float) 
    True
    >>> isinstance(z, Real)  
    False
    '''

    def __init__(self, value):
        super().__init__(value, 0)
        
    def __mul__(self, other):
        """Multiply a Complex number"""
        #(x+yi) * real = (x*real) + (y*real)i
        if isinstance(other, Real):
            #(x+yi) * (u+vi) = (xu-yv) + (xv+yu)i
            a = self._real * other._real - self._imag * other._imag
            ans = Real(a)
        elif isinstance(other, Complex):
            ans = Complex.__mul__(self, other)
        else:
            a = self._real * other
            ans = Real(a)
            
        return ans
    
    __rmul__ = __mul__
    
    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        if isinstance(self, Real) and isinstance(other, Real):
            if self._real == other._real:
                return True
            else:
                return False
        elif isinstance(other, Complex):
            if self._real == other._real and self._imag == other._imag:
                return True
            else: 
                return False
        else:
            return False
        
    def __int__(self):
        return int(self._real)
    
    def __float__(self):
        return float(self._real)
            

if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(StudentAccount, globals(), name='HW22',verbose=True) # replace Course for the class name you want to test