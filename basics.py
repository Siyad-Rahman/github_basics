"""
Basic Python Code Examples
This file demonstrates fundamental Python concepts
"""

# Variables and Data Types
name = "Python"
age = 30
height = 5.9
is_student = True

# Lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]

# Dictionary
person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# Functions
def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

def calculate_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

# Conditional Statements
def check_age(age):
    """Check if person is an adult"""
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

# Loops
def print_fruits():
    """Print all fruits"""
    for fruit in fruits:
        print(f"Fruit: {fruit}")

def sum_numbers():
    """Sum all numbers in the list"""
    total = 0
    for num in numbers:
        total += num
    return total

# List Comprehension
squared_numbers = [x**2 for x in numbers]

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
    print(f"Squared numbers: {squared_numbers}\n")
    
    # Dictionary access
    print("Person details:")
    for key, value in person.items():
        print(f"{key.capitalize()}: {value}")
