# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        self.cdata = (cid, cname, credits)

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"{self.cdata[0]}({self.cdata[2]}): {self.cdata[1]}"

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        is_same = False
        
        if other is not None:
            if self.cdata[0] == other.cdata[0]:
                is_same = True
                
        return is_same


class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400), 'CMPSC360': (CMPSC360(3): Discrete Mathematics, 200)}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400)}
        >>> isinstance(C.courseOfferings['CMPSC132'][0], Course)
        True
    '''

    def __init__(self):
        # YOUR CODE STARTS HERE
        self.course_catalog = {}

    def addCourse(self, cid, cname, credits, capacity):
        # YOUR CODE STARTS HERE
        course = Course(cid, cname, credits)
        self.course_catalog.update({cid: (course, capacity)})
        
        return "Course added successfully"

    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        if cid in self.course_catalog.keys():
            self.course_catalog.pop(cid)
            return "Course removed successfully"
    
    @property
    def courseOfferings(self):
        return self.course_catalog


class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> isinstance(semester.courses['CMPSC132'], Course)
        True
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.courses
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''

    def __init__(self, sem_num):
        # --- YOUR CODE STARTS HERE
        self.sem_num = sem_num
        self.courses = {}

    def __str__(self):
        # YOUR CODE STARTS HERE
        if self.courses:
            return ", ".join(self.courses.keys())
        else:
            return "No courses"

    __repr__ = __str__

    def addCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cdata[0].upper() not in self.courses.keys():
            self.courses.update({course.cdata[0].upper(): course})
        else:
            return "Course already added"

    def dropCourse(self, course):
        # YOUR CODE STARTS HERE
        if course.cdata[0].upper() in self.courses.keys():
            self.courses.pop(course.cdata[0].upper())
        else:
            return "No such course"

    @property
    def totalCredits(self):
        # YOUR CODE STARTS HERE
        credits = 0
        
        if self.courses:
            for course in self.courses.values():
                credits += course.cdata[2]
                
        return credits

    @property
    def isFullTime(self):
        # YOUR CODE STARTS HERE
        return False if self.totalCredits < 12 else True

    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        # YOUR CODE STARTS HERE
        self.amount = amount
        self.loan_id = self.__getloanID

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Balance: ${self.amount}"

    __repr__ = __str__

    @property
    def __getloanID(self):
        # YOUR CODE STARTS HERE
        return random.randrange(10000, 100000)


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        # YOUR CODE STARTS HERE
        self.name = name
        self.ssn = ssn

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Person({self.name}, ***-**-{self.ssn[-4:]})"

    __repr__ = __str__

    def get_ssn(self):
        # YOUR CODE STARTS HERE
        return self.ssn

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        return True if self.ssn == other.ssn else False


class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        # YOUR CODE STARTS HERE
        self.name = name
        self.ssn = ssn
        self.supervisor = supervisor
        self.hold = False

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Staff({self.name}, {self.id})"

    __repr__ = __str__


    @property
    def id(self):
        # YOUR CODE STARTS HERE 
        #Making a list of of initials char determined by capitalized letter               
        initials = [char.lower() for char in self.name if char.isupper()]
        
        return f"905{''.join(initials)}{self.ssn[-4:]}"

    @property   
    def getSupervisor(self):
        # YOUR CODE STARTS HERE
        return self.supervisor

    def setSupervisor(self, new_supervisor):
        # YOUR CODE STARTS HERE
        if isinstance(new_supervisor, Staff):
            self.supervisor = new_supervisor
            return "Completed!"


    def applyHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = True
            return "Completed!"

    def removeHold(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.hold = False
            return "Completed!"

    def unenrollStudent(self, student):
        # YOUR CODE STARTS HERE
        if isinstance(student, Student):
            student.active = False
            return "Completed!"

    def createStudent(self, person):
        # YOUR CODE STARTS HERE
        return Student(person.name, person.ssn, year="Freshman")
    

class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        # YOUR CODE STARTS HERE
        self.name = name
        self.ssn = ssn
        self.year = year
        self.current_sem = 0
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()
        
    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Student({self.name}, {self.id}, {self.year})"

    __repr__ = __str__

    def __createStudentAccount(self):
        # YOUR CODE STARTS HERE
        if self.active:
            return StudentAccount(self)

    @property
    def id(self):
        # YOUR CODE STARTS HERE
        initials = [char.lower() for char in self.name if char.isupper()]
        
        return f"{''.join(initials)}{self.ssn[-4:]}"

    def registerSemester(self):
        # YOUR CODE STARTS HERE
        if not self.hold and self.active:
            #Updating the semester dictionary
            self.current_sem += 1
            semester = Semester(self.current_sem)
            self.semesters.update({self.current_sem: semester})
            
            #Determine the year of the student
            if self.semesters:
                sem_num = len(self.semesters.keys())
            if self.current_sem <= 2:
                self.year = "Freshman"
            elif self.current_sem <= 4:
                self.year = "Sophomore"
            elif self.current_sem <= 6:
                self.year = "Junior"
            else:
                self.year = "Senior"
        else:
            return "Unsuccessful operation"

    def enrollCourse(self, cid, catalog, semester):
        # YOUR CODE STARTS HERE
        self.current_sem = semester
        if not self.active or self.hold:
            return "Unsuccessful operation"
        elif cid not in catalog.course_catalog.keys():
            return "Course not found"
        else:
            course = catalog.course_catalog.get(cid)[0]
            if self.semesters.get(semester) is None:    #No course enrolled yet
                semester_obj = Semester(semester)
                semester_obj.addCourse(course)
            else:                                       #There are courses enrolled
                semester_obj = self.semesters.get(semester)
                if cid in semester_obj.courses.keys():
                    return "Course already enrolled"
                else:
                    #Add course
                    semester_obj.addCourse(course)
                    self.semesters.update({semester: semester_obj})
                    #Charge money
                    cost = course.cdata[2] * self.account.CREDIT_PRICE
                    self.account.chargeAccount(cost)
                    return "Course added successfully"
    
    def dropCourse(self, cid):
        # YOUR CODE STARTS HERE
        if not self.active or self.hold:
            return "Unsuccessful operation"
        elif cid not in self.semesters.get(self.current_sem).courses.keys():
            return "Course not found"
        else:
            #Refund money
            refund = self.semesters.get(self.current_sem).courses.get(cid).cdata[2] * self.account.CREDIT_PRICE / 2
            self.account.makePayment(refund)
            #Remove course
            self.semesters.get(self.current_sem).courses.pop(cid)

            return "Course dropped successfully"

    def getLoan(self, amount):
        # YOUR CODE STARTS HERE
        if self.active and self.semesters.get(self.current_sem).isFullTime:
            loan = Loan(amount)
            self.account.makePayment(amount)
            self.account.loans.update({loan.loan_id: loan})

class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4, 600)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2, 500)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4, 300)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    CREDIT_PRICE = 1000
    
    def __init__(self, student):
        # YOUR CODE STARTS HERE
        self.student = student
        self.balance = 0
        self.loans = {}

    def __str__(self):
        # YOUR CODE STARTS HERE
        return f"Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}"

    __repr__ = __str__

    def makePayment(self, amount):
        # YOUR CODE STARTS HERE
        self.balance -= amount
        return self.balance

    def chargeAccount(self, amount):
        # YOUR CODE STARTS HERE
        self.balance += amount
        return self.balance

if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    #doctest.run_docstring_examples(StudentAccount, globals(), name='HW22',verbose=True) # replace Course for the class name you want to test