
https://onlinegdb.com/RJgKXd1Nw

![alt text](<Screenshot 2026-10-07 095255.png>)




Personal Data Collector 🐍

A beginner-friendly Python program that collects personal information from the user and demonstrates variables, data types, type casting, arithmetic operations, and basic Python functions.

📌 Project Overview

The Personal Data Collector asks the user to enter:

Name

Age

Height in meters

Favourite number

It then processes the information and displays:

Variable values

Data types

Memory addresses

Arithmetic calculations

Type casting

Estimated birth year

A final personal data summary

✨ Features

📝 Collects user input using input()

🔢 Converts input into int and float

🧮 Performs basic arithmetic operations

🔄 Demonstrates type casting

🧠 Displays Python variable types using type()

💾 Displays variable memory addresses using id()

📅 Calculates the user's birth year

📊 Displays a formatted personal data summary

🛠️ Concepts Demonstrated

This project is designed to practice the following Python concepts:

Variables

User Input

Data Types

str

int

float

Type Conversion / Type Casting

Arithmetic Operators

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

Formatted Strings (f-strings)

type() Function

id() Function

Basic Calculations

Formatted Console Output

📋 Requirements

You only need:

Python 3.x

No external libraries or packages are required.

▶️ How to Run
1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

python --version


or:

python3 --version

2. Save the Program

Save the Python code in a file such as:

personal_data_collector.py

3. Run the Program

Use:

python personal_data_collector.py


or:

python3 personal_data_collector.py

💻 Example
Input
==================================================
WELCOME TO THE PERSONAL DATA COLLECTOR
==================================================

Enter your name: Rahul
Enter your age: 20
Enter your height in meters: 1.75
Enter your favourite number: 5

Output
Data collected successfully!

==================================================
VARIABLE INFORMATION
==================================================

Name = Rahul
Type: <class 'str'>
Memory Address: ...

Age = 20
Type: <class 'int'>
Memory Address: ...

Height = 1.75
Type: <class 'float'>
Memory Address: ...

Favourite Number = 5
Type: <class 'int'>
Memory Address: ...

==================================================
ARITHMETIC OPERATIONS
==================================================

Age + Favourite Number = 25
Age - Favourite Number = 15
Age * Favourite Number = 100
Age / Favourite Number = 4.0

==================================================
TYPE CASTING
==================================================

Original Height: 1.75 Type: <class 'float'>
Height converted to Integer: 1
Type after conversion: <class 'int'>

==================================================
PERSONAL DATA SUMMARY
==================================================

Name            : Rahul
Age             : 20
Height          : 1.75 meters
Favourite Number: 5
Birth Year      : 2006

Thank you for using the Personal Data Collector!
Keep learning Python. Goodbye!


Note: The memory addresses shown by id() will be different each time the program runs.

📂 Project Structure
Personal-Data-Collector/
│
├── personal_data_collector.py
└── README.md

⚠️ Important Notes

The program expects the age and favourite number to be valid integers.

The height should be entered as a number such as 1.75.

The current year is manually set to 2026 in the program.

The birth year is calculated as:

Birth Year = Current Year - Age


The height conversion from float to int removes the decimal portion. For example:

1.75 → 1

🎯 Learning Objective

The main goal of this project is to help beginners understand how Python handles:

User input

Variables

Different data types

Type conversion

Mathematical operations

Basic output formatting

🚀 Future Improvements

Possible improvements include:

Add input validation

Automatically detect the current year

Handle invalid user input with try-except

Calculate BMI

Add more personal information

Store the collected data in a file

Create a graphical user interface (GUI)

👨‍💻 Author

Your Name

A beginner Python project created for learning and practicing fundamental Python programming concepts.

📄 License

This project is created for educational purposes.