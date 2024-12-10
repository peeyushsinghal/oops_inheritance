# OOP Inheritance Demo

This project demonstrates Object-Oriented Programming (OOP) concepts in Python, specifically focusing on inheritance, property decorators, and class relationships.

## Project Structure

- `oopsinheritance.py`: Contains the main class implementations
- `test_oopsinheritance.py`: Contains unit tests for all classes
- `README.md`: Project documentation (this file)

## Classes Overview

### Person
Base class that implements common attributes for all persons:
- Properties: name, age, job
- All properties have getters and setters with validation
- Method: `get_details()` returns formatted string of person details

### Student (inherits from Person)
- Adds grade attribute
- Overrides `get_details()` to include grade information

### Professor (inherits from Person)
- Adds courses attribute (list of courses)
- Properties: courses with getter/setter
- Overrides `get_details()` to include courses information

### Employee (inherits from Person)
- Adds department attribute
- Overrides `get_details()` to include department information

### StudentProfessor (inherits from Student and Professor)
- Example of multiple inheritance
- Combines attributes from both Student and Professor
- Custom implementation of `get_details()`

### Location
- Uses `__slots__` for memory optimization
- Stores name and coordinates (latitude, longitude)
- Method: `get_coordinates()` returns tuple of coordinates

## Usage Example 
```python
# Create a StudentProfessor instance
student_professor = StudentProfessor("Dr. White", 60, "Professor", ["Engineering"], "A")
print(student_professor.get_details())
Output: "Name: Dr. White, Age: 60, Job: Professor, Courses: ['Engineering'], Grade: A"
```

```python
# Create a Location instance
location = Location("Paris", 48.8566, 2.3522)
coordinates = location.get_coordinates()
Returns: (48.8566, 2.3522)
```

## Running Tests

Tests are implemented using pytest. To run the tests:
```bash
pytest test_oopsinheritance.py
```

The test suite covers:
- Basic functionality of all classes
- Inheritance relationships
- Property validation
- Slots implementation
- Multiple inheritance

## Requirements

- Python 3.x
- pytest (for running tests)
