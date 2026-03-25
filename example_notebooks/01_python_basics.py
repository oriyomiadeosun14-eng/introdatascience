import marimo

__generated_with = "0.20.4"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Python Basics for Data Science 🐍

    **Welcome!** This notebook will teach you essential Python concepts needed for data science.

    **What you'll learn:**

    - Variables and data types
    - Lists and dictionaries
    - Control flow (if/else, loops)
    - Functions

    **Estimated time:** 45 minutes

    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1. Variables and Data Types
    """)
    return


@app.cell
def _():
    # Variables store data
    name = "Ninety"
    age = 25
    height = 1.65  # in meters
    is_student = True

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height}m")
    print(f"Is student: {is_student}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Data Types

    Python has several basic data types:

    - **str** (string): Text data like `"Hello"`
    - **int** (integer): Whole numbers like `42`
    - **float**: Decimal numbers like `3.14`
    - **bool** (boolean): `True` or `False`
    """)
    return


@app.cell
def _():
    # Check types
    print(type("This is a string"))  # str
    print(type(42))       # int
    print(type(3.14))     # float
    print(type(True))     # bool
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2. Basic Operations
    """)
    return


@app.cell
def _():
    # Math operations
    x = 10
    y = 3

    print(f"Addition: {x} + {y} = {x + y}")
    print(f"Subtraction: {x} - {y} = {x - y}")
    print(f"Multiplication: {x} * {y} = {x * y}")
    print(f"Division: {x} / {y} = {x / y}")
    print(f"Integer division: {x} // {y} = {x // y}")
    print(f"Modulo (remainder): {x} % {y} = {x % y}")
    print(f"Power: {x} ** {y} = {x ** y}")
    return


@app.cell
def _():
    # String operations
    first_name = "Oriyomi"
    last_name = "Adeosun"

    full_name = first_name + " " + last_name  # Concatenation
    print(f"Full name: {full_name}")
    print(f"Uppercase: {full_name.upper()}")
    print(f"Length: {len(full_name)} characters")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3. Lists - Ordered Collections
    """)
    return


@app.cell
def _():
    # Create a list
    fruits = ["apple", "banana", "cherry", "date"]
    print("Fruits:", fruits)

    # Access by index (starts at 0)
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")

    # Add to list
    fruits.append("orange")
    print("After append:", fruits)

    # List length
    print(f"Number of fruits: {len(fruits)}")
    return (fruits,)


@app.cell
def _(fruits):
    # List slicing
    print(f"First 3: {fruits[:3]}")
    print(f"Last 2: {fruits[-2:]}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4. Dictionaries - Key-Value Pairs
    """)
    return


@app.cell
def _():
    # Create a dictionary
    student = {
        "name": "Bob",
        "age": 22,
        "grade": "A",
        "courses": ["Math", "Physics", "CS"]
    }

    print("Student:", student)
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Courses: {student['courses']}")
    return (student,)


@app.cell
def _(student):
    # Add/modify dictionary entries
    student["email"] = "bob@example.com"
    student["age"] = 23  # Update age

    print("Updated student:", student)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 5. Control Flow - If/Else
    """)
    return


@app.cell
def _():
    score = 85

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Score: {score} → Grade: {grade}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 6. Loops - For Loop
    """)
    return


@app.cell
def _(fruits):
    # Loop through a list
    print("Fruits in my basket:")
    for fruit in fruits:
        print(f"  - {fruit}")

    def calculate_area(width,height):
        return width * height
        print(calculate_area)

    calculate_area(5,4 )

    return


@app.cell
def _():
    # Loop with range
    print("\nCounting to 5:")
    for i in range(1, 6):
        print(i)
    return


@app.cell
def _():
    # Loop with calculation
    numbers = [1, 2, 3, 4, 5]
    total = 0

    for num in numbers:
        total += num

    print(f"Sum of {numbers} = {total}")
    return (numbers,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 7. List Comprehensions - Elegant Loops
    """)
    return


@app.cell
def _(numbers):
    # Create a new list from an existing one
    # Traditional way
    squares_traditional = []
    for n in numbers:
        squares_traditional.append(n ** 2)

    # List comprehension way (more Pythonic!)
    squares = [n ** 2 for n in numbers]

    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")
    return


@app.cell
def _():
    # Filter with list comprehension
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [n for n in number_list if n % 2 == 0]

    print(f"Even numbers: {even_numbers}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 8. Functions - Reusable Code
    """)
    return


@app.cell
def _():
    # Define a function
    def greet(name):
        """Greet someone by name"""
        return f"Hello, {name}!"

    # Use the function
    message = greet("Alice")
    print(message)

    message2 = greet("Bob")
    print(message2)
    return


@app.cell
def _():
    # Function with multiple parameters
    def calculate_bmi(weight_kg, height_m):
        """Calculate Body Mass Index"""
        bmi = weight_kg / (height_m ** 2)
        return round(bmi, 1)

    bmi = calculate_bmi(70, 1.75)
    print(f"BMI: {bmi}")
    return


@app.cell
def _():
    # Function with default parameters
    def create_greeting(name, greeting="Hello"):
        """Create a custom greeting"""
        return f"{greeting}, {name}!"

    print(create_greeting("Alice"))
    print(create_greeting("Bob", "Hi"))
    print(create_greeting("Charlie", "Hey"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 9. Putting It All Together

    Let's use everything we learned to analyze some data!
    """)
    return


@app.cell
def _():
    # Candidate data
    candidates = [
        {"name": "Alice", "scores": [85, 90, 88]},
        {"name": "Bob", "scores": [78, 82, 80]},
        {"name": "Charlie", "scores": [92, 95, 93]},
    ]

    # Function to calculate average
    def calculate_average(scores):
        """Calculate the average of a list of numbers"""
        return sum(scores) / len(scores)

    # Analyze each candidate
    print("Candidate Averages:")
    for candidate in candidates:
        avg = calculate_average(candidate['scores'])
        print(f"  {candidate['name']}: {avg:.1f}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🎉 Congratulations!

    You've learned the Python basics! You now know:

    - ✅ Variables and data types
    - ✅ Basic operations
    - ✅ Lists and dictionaries
    - ✅ If/else statements
    - ✅ For loops
    - ✅ List comprehensions
    - ✅ Functions

    **Next step:** Open `02_data_wrangling.py` to learn about working with real datasets!
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
