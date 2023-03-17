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
        