class Person:
    """
    Base class representing a person with basic attributes.

    Attributes:
        _name (str): Person's full name
        _age (int): Person's age (must be positive)
        _job (str): Person's occupation
    """

    def __init__(self, name: str, age: int, job: str) -> None:
        """
        Initialize a Person instance.

        Args:
            name (str): Person's full name
            age (int): Person's age
            job (str): Person's occupation
        """
        self._name = name
        self._age = age
        self._job = job

    @property
    def name(self) -> str:
        """Get person's name."""
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        """
        Set person's name.

        Args:
            value (str): New name value
        
        Raises:
            ValueError: If name is not a string
        """
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")
    
    @property
    def age(self) -> int:
        """Get person's age."""
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        """
        Set person's age.

        Args:
            value (int): New age value
        
        Raises:
            ValueError: If age is not a positive integer
        """
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError("Age must be a positive integer")
    
    @property
    def job(self) -> str:
        """Get person's job."""
        return self._job
    
    @job.setter
    def job(self, value: str) -> None:
        """
        Set person's job.

        Args:
            value (str): New job value
        
        Raises:
            ValueError: If job is not a string
        """
        if isinstance(value, str):
            self._job = value
        else:
            raise ValueError("Job must be a string")
    
    def get_details(self) -> str:
        """
        Get formatted string of person's details.

        Returns:
            str: Formatted string containing name, age, and job
        """
        return f"Name: {self._name}, Age: {self._age}, Job: {self._job}"


class Student(Person):
    """
    Class representing a student, inheriting from Person.

    Additional Attributes:
        _grade (str): Student's academic grade
    """

    def __init__(self, name: str, age: int, job: str, grade: str) -> None:
        """
        Initialize a Student instance.

        Args:
            name (str): Student's name
            age (int): Student's age
            job (str): Student's occupation
            grade (str): Student's grade
        """
        super().__init__(name, age, job)
        self._grade = grade

    def get_details(self) -> str:
        """
        Get formatted string of student's details.

        Returns:
            str: Formatted string containing person details and grade
        """
        return super().get_details() + f", Grade: {self._grade}"


class Professor(Person):
    """
    Class representing a professor, inheriting from Person.

    Additional Attributes:
        _courses (list): List of courses taught by professor
    """

    def __init__(self, name: str, age: int, job: str, courses: list) -> None:
        """
        Initialize a Professor instance.

        Args:
            name (str): Professor's name
            age (int): Professor's age
            job (str): Professor's occupation
            courses (list): List of courses taught
        """
        super().__init__(name, age, job)
        self._courses = courses
    
    @property
    def courses(self) -> list:
        """Get professor's courses."""
        return self._courses
    
    @courses.setter
    def courses(self, value: list) -> None:
        """
        Set professor's courses.

        Args:
            value (list): New list of courses
        
        Raises:
            ValueError: If courses is not a list
        """
        if isinstance(value, list):
            self._courses = value
        else:
            raise ValueError("Courses must be a list")
    
    def get_details(self) -> str:
        """
        Get formatted string of professor's details.

        Returns:
            str: Formatted string containing person details and courses
        """
        return super().get_details() + f", Courses: {self._courses}"


class Employee(Person):
    """
    Class representing an employee, inheriting from Person.

    Additional Attributes:
        _department (str): Employee's department
    """

    def __init__(self, name: str, age: int, job: str, department: str) -> None:
        """
        Initialize an Employee instance.

        Args:
            name (str): Employee's name
            age (int): Employee's age
            job (str): Employee's occupation
            department (str): Employee's department
        """
        super().__init__(name, age, job)
        self._department = department
    
    def get_details(self) -> str:
        """
        Get formatted string of employee's details.

        Returns:
            str: Formatted string containing person details and department
        """
        return super().get_details() + f", Department: {self._department}"


class StudentProfessor(Student, Professor):
    """
    Class representing someone who is both a student and professor.
    Demonstrates multiple inheritance.

    Attributes:
        Inherits from both Student and Professor
    """

    def __init__(self, name: str, age: int, job: str, courses: list, grade: str) -> None:
        """
        Initialize a StudentProfessor instance.

        Args:
            name (str): Name
            age (int): Age
            job (str): Occupation
            courses (list): List of courses taught
            grade (str): Academic grade
        """
        Person.__init__(self, name, age, job)
        self.courses = courses
        self.grade = grade
    
    def get_details(self) -> str:
        """
        Get formatted string of student-professor's details.

        Returns:
            str: Formatted string containing all details
        """
        return (f"Name: {self.name}, Age: {self.age}, Job: {self.job}, "
                f"Courses: {self.courses}, Grade: {self.grade}")


class Location:
    """
    Class representing a geographical location.
    Uses __slots__ for memory optimization.

    Attributes:
        name (str): Location name
        latitude (float): Geographical latitude
        longitude (float): Geographical longitude
    """
    
    __slots__ = ["name", "latitude", "longitude"]

    def __init__(self, name: str, latitude: float, longitude: float) -> None:
        """
        Initialize a Location instance.

        Args:
            name (str): Location name
            latitude (float): Geographical latitude
            longitude (float): Geographical longitude
        """
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def get_coordinates(self) -> tuple:
        """
        Get location coordinates.

        Returns:
            tuple: Pair of (latitude, longitude) coordinates
        """
        return (self.latitude, self.longitude)


