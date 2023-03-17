# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

import random

class Fibonacci:
    """
        >>> fib_seq = Fibonacci()
        >>> fib_seq
        <Fibonacci object>, value = 0
        >>> fib_seq.next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next()
        <Fibonacci object>, value = 1
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next()
        <Fibonacci object>, value = 2
        >>> fib_seq.next().next().next().next()
        <Fibonacci object>, value = 3
        >>> fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
        >>> other_fib_seq = Fibonacci()
        >>> other_fib_seq
        <Fibonacci object>, value = 0
        >>> other_fib_seq.next().next().next().next().next()
        <Fibonacci object>, value = 5
        >>> fib_seq.next().next().next().next().next().next()
        <Fibonacci object>, value = 8
    """

    def __init__(self):
        self.start = 0


    def next(self):
        #--- YOUR CODE STARTS HERE        
        copy_fib = Fibonacci()
        
        if self.start == 0:
            #Setting up for the first Fibonacci
            Fibonacci._prev = 0
            copy_fib.start = 1
        else:
            #Taking the previous value adding with the current value to get the next Fib in the sequence
            copy_fib.start = self.start + Fibonacci._prev
            Fibonacci._prev = self.start

        return copy_fib

    def __repr__(self):
        return f"<Fibonacci object>, value = {self.start}"


class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10'
        >>> east_machine.cancelTransaction()
        'Take your $10 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''

    def __init__(self):
        #--- YOUR CODE STARTS HERE
        self._stock = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        self._balance = 0

    def purchase(self, item, qty=1):
        #--- YOUR CODE STARTS HERE        
        if item not in self._stock.keys():
            return "Invalid item"
        
        elif not self.isStocked:
            return "Machine out of stock"
        
        elif self._stock.get(item)[1] == 0:
            return "Item out of stock"
        
        elif qty > self._stock.get(item)[1]:
            return f"Current {item} stock: {self._stock.get(item)[1]}, try again"
        
        elif self._balance < self._stock.get(item)[0]*qty:
            return f"Please deposit ${self._stock.get(item)[0]*qty - self._balance}"
        
        elif self._balance >= self._stock.get(item)[0]*qty:
            #Decrease stock
            item_data = self._stock.get(item)
            item_data[1] -= qty
            self._stock.update({item:item_data})
            #Decrease money
            self._balance -= self._stock.get(item)[0]*qty
            if self._balance == 0:
                self._balance = 0
                return "Item dispensed"
            else:
                #Reset balance to 0 after dispensing
                balance_return = self._balance
                self._balance = 0
                return f"Item dispensed, take your ${balance_return} back"
        
    def deposit(self, amount):
        #--- YOUR CODE STARTS HERE
        if not self.isStocked:
            return f"Machine out of stock. Take your ${amount} back"
        else:
            self._balance += amount
            return f"Balance: ${self._balance}"
            
    def _restock(self, item, stock):
        #--- YOUR CODE STARTS HERE
        if item not in self._stock.keys():
            return "Invalid item"
        else:
            #Getting the data of the item and increase stock
            item_data = self._stock.get(item)
            item_data[1] += stock
            self._stock.update({item:item_data})

            return f"Current item stock: {item_data[1]}"

    #--- YOUR CODE STARTS HERE
    @property
    def isStocked(self):
        is_stock = True
        count_not_stock = 0
        
        #Loop through to check how many item is not stocked
        for item_data in self._stock.values():
            if item_data[1] == 0:
                count_not_stock += 1
        
        if count_not_stock == len(self._stock.keys()):
            is_stock = False
            
        return is_stock
            
    #--- YOUR CODE STARTS HERE
    @property
    def getStock(self):
        return self._stock


    def cancelTransaction(self):
        #--- YOUR CODE STARTS HERE
        if self._balance == 0:
            return None
        else: 
            balance_return = self._balance
            self._balance = 0
            return f"Take your ${abs(balance_return)} back"
       


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = 4*line1
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
    '''
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self._start_x = point1.x
        self._start_y = point1.y
        self._end_x = point2.x
        self._end_y = point2.y

    #--- YOUR CODE STARTS HERE
    @property
    def getDistance(self):
        distance = ((self._end_x - self._start_x)**2 + (self._end_y-self._start_y)**2)**(1/2)

        return round(distance, 3)
    
    #--- YOUR CODE STARTS HERE
    @property
    def getSlope(self):
        top = self._end_y - self._start_y
        bottom = self._end_x - self._start_x
        if bottom == 0:
            return float("inf")
        else:
            slope = top/bottom
            
            return round(slope, 3)
        
    #--- YOUR CODE CONTINUES HERE
    def __str__(self):
        #Formating a string as a line equation
        if self.getSlope == float("inf"):
            return "Undefined"
        else:
            b = self._start_y - (self.getSlope * self._start_x)

            if self.getSlope == 0:
                return f"y = {round(b, 3)}"
            else:
                return f"y = {self.getSlope}x + {round(b, 3)}"

    __repr__ = __str__
    
    def __mul__(self, mult):
        start_x = mult * self._start_x
        start_y = mult * self._start_y
        end_x = mult * self._end_x
        end_y = mult * self._end_y
        point1 = Point2D(start_x, start_y)
        point2 = Point2D(end_x, end_y)
        
        return Line(point1, point2)
    
    __rmul__ = __mul__
        
    def __eq__(self, other):
        if isinstance(self, Line) and isinstance(other, Line):
            if (self._start_x == other._start_x) and (self._start_y == other._start_y) and (self._end_x == other._end_x) and (self._end_y == other._end_y):
               return True
            else:
               return False
        else:
            return False
               
        

if __name__=='__main__':
    import doctest
    #doctest.testmod()  # OR
    doctest.run_docstring_examples(Line, globals(), name='LAB2',verbose=True) # replace Fibonacci for the class name you want to test