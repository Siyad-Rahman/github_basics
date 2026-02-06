"""
Basic Python Code Examples
This file demonstrates fundamental Python concepts
"""

from typing import List, Dict, Optional, Any, Generator, Callable
from dataclasses import dataclass
from datetime import datetime, timedelta
from contextlib import contextmanager
import json
import os

# Variables and Data Types
name: str = "Python Dev"
age: int = 30
height: float = 5.9
is_student: bool = True

# Lists
fruits: List[str] = ["apple", "banana", "orange"]
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuples (immutable)
coordinates: tuple[int, int] = (10, 20)
rgb_color: tuple[int, int, int] = (255, 128, 0)

# Sets (unique elements)
unique_numbers: set[int] = {1, 2, 3, 4, 5, 5, 4}  # Duplicates removed
programming_languages: set[str] = {"Python", "JavaScript", "Java", "Python"}

# Dictionary
person: Dict[str, Any] = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# Functions with type hints
def greet(name: str) -> str:
    """Function to greet a person"""
    return f"Hello, {name}!"

def add_numbers(a: int, b: int) -> int:
    """Function to add two numbers"""
    return a + b

def calculate_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle"""
    return length * width

# Conditional Statements
def check_age(age: int) -> str:
    """Check if person is an adult"""
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

# Loops
def print_fruits() -> None:
    """Print all fruits"""
    for fruit in fruits:
        print(f"Fruit: {fruit}")

def sum_numbers() -> int:
    """Sum all numbers in the list"""
    total = 0
    for num in numbers:
        total += num
    return total

# List Comprehension
squared_numbers: List[int] = [x**2 for x in numbers]
even_numbers: List[int] = [x for x in numbers if x % 2 == 0]

# Dictionary Comprehension
fruit_lengths: Dict[str, int] = {fruit: len(fruit) for fruit in fruits}
fruit_prices: Dict[str, float] = {fruit: len(fruit) * 0.5 for fruit in fruits}

# Set Comprehension
unique_squares: set[int] = {x**2 for x in numbers}

# Lambda Functions
square: Callable[[int], int] = lambda x: x**2
add: Callable[[int, int], int] = lambda a, b: a + b
is_even: Callable[[int], bool] = lambda x: x % 2 == 0

# Using lambda with built-in functions
sorted_fruits: List[str] = sorted(fruits, key=lambda x: len(x))
filtered_numbers: List[int] = list(filter(lambda x: x > 2, numbers))
mapped_numbers: List[int] = list(map(lambda x: x * 2, numbers))

# Class Example
@dataclass
class Student:
    """A simple Student class using dataclass"""
    name: str
    age: int
    grade: float
    
    def get_info(self) -> str:
        """Return student information"""
        return f"{self.name}, age {self.age}, grade: {self.grade}"
    
    def is_passing(self, passing_grade: float = 60.0) -> bool:
        """Check if student is passing"""
        return self.grade >= passing_grade

# Error Handling Example
def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers with error handling"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Invalid input types!")
        return None

# Main execution block
if __name__ == "__main__":
    print("=== Basic Python Examples ===\n")
    
    # Print variables
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height}")
    print(f"Is Student: {is_student}\n")
    
    # Function calls
    print(greet("World"))
    print(f"Sum of 5 and 3: {add_numbers(5, 3)}")
    print(f"Area of rectangle (4x5): {calculate_area(4, 5)}\n")
    
    # Conditional example
    print(f"Age check (25): {check_age(25)}")
    print(f"Age check (15): {check_age(15)}\n")
    
    # Loop examples
    print("Fruits:")
    print_fruits()
    print(f"\nSum of numbers: {sum_numbers()}")
    print(f"Squared numbers: {squared_numbers}")
    print(f"Fruit lengths: {fruit_lengths}\n")
    
    # Dictionary access
    print("Person details:")
    for key, value in person.items():
        print(f"{key.capitalize()}: {value}")
    
    # Class example
    print("\n=== Class Example ===")
    student1 = Student("Alice", 20, 85.5)
    student2 = Student("Bob", 19, 55.0)
    print(student1.get_info())
    print(f"Is passing: {student1.is_passing()}")
    print(student2.get_info())
    print(f"Is passing: {student2.is_passing()}\n")
    
    # Error handling example
    print("=== Error Handling Example ===")
    result1 = safe_divide(10, 2)
    print(f"10 / 2 = {result1}")
    result2 = safe_divide(10, 0)
    print(f"10 / 0 = {result2}")
    result3 = safe_divide(15, 3)
    print(f"15 / 3 = {result3}")
