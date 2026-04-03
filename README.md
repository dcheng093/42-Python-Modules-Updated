*This project has been created as part of the 42 curriculum by dcheng.*
# Python Module Overview

Welcome to your Python learning journey! This repository collects exercises from the Python Modules from 00 to 10, each module builds on the previous, gradually increasing complexity while teaching practical programming skills. It also teaches you how to endure psychological torture, so... Just a normal 42 project.

Keep in mind, this README.md was written in early January 2026, a lot of the exercises have changed and therefore the contents and examples I will be providing will be slightly outdated.

<p align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW1kdjZwM2h2YXQzZHQ2NGZ1ZDl5aDRncms4d2Rla2UzdHF1dGFrZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/O8dCwBMsKWwtfrcgQs/giphy.gif" alt="cute gif" width="300"/>
</p>

---

## Table of Contents 📚

1. [More info](#more-info)  
2. [Module 00 : Growing Code Python Fundamentals 🌱](#module-00--growing-code-python-fundamentals)
3. [Module 01 : Code Cultivation 🌿](#module-01--code-cultivation)  
4. [Module 02 : Garden Guardian Data Engineering for Smart Agriculture 🌾](#module-02--garden-guardian-data-engineering-for-smart-agriculture)  
5. [Module 03 : Data Quest The Pixel Dimension 🎮](#module-03--data-quest-the-pixel-dimension)  
6. [Module 04 : Cyber Archives Training Program 🗄️](#module-04--cyber-archives-training-program)  
7. [Module 05 : Nexus Stream Engineer Training 🚀](#module-05--nexus-stream-engineer-training)  
8. [Instructions 🛠️](#instructions)  
9. [Use of AI 🤖](#use-of-ai)  
10. [Skills Gained Summary 🎯](#skills-gained-summary)  

---

## More info

This curriculum guides you through six progressive Python learning modules. You’ll start with core Python syntax and functions, then advance into object-oriented programming, data structures, secure file handling, and finally complex stream processing systems. Each module is designed to build practical skills, using analogies like gardens, game worlds, and digital archives. Unless you didn't read any of them and don't care about the storyline... I still haven't actually read any of them

---

## Module 00 : Growing Code Python Fundamentals

**Theme:** Community Garden Scenarios  
**Focus:** Python core concepts  

The main thing that stood out to me while doing this project was how much I had forgotten Python's syntax. Overall this module this module was helpful in terms of getting comfortable with writing in Python again, and teaches you some in-built functions as well.

### What You Learn:
- Writing Python functions without `main` blocks  
- Basic syntax: variables, operators, loops, conditionals  
- Handling input and output through functions  
- Following coding standards (flake8)  
- Structuring code for clarity and readability  
- Optional: type hints for better understanding
- False hope - ("Wow these python modules are pretty fun and easy! They must be a nice break from all that hardwork I did in Milestone 1!")

> 💡 This module is all about planting the seeds of Python knowledge. Each exercise is a small, contained function to strengthen your foundational skills.

---

## Module 01 : Code Cultivation

**Theme:** Digital Garden Data Management  
**Focus:** Program structure & Object-Oriented Programming  

This module introduces classes, which are essentially blueprints for creating objects. A class defines both the attributes (data) and behavior (functions/methods) that the objects created from it will have. Attributes are the properties that describe the state of an object. In Python, they are usually defined in the __init__ method (the constructor), which runs automatically when an object is created. For example:
```python
class Plant:
    def __init__(self, name, height):
        self.name = name       # attribute
        self.height = height   # attribute

    def grow(self, amount):
        self.height += amount  # behavior: changes the object's state
```
Here, **name** and **height** are attributes that store information about the **Plant** object. Behavior refers to the methods defined within the class. These are functions that can perform actions or modify the object's attributes, as seen with **grow**. Using classes and objects allows you to organize complex data and reuse code more naturally. For instance, you can create multiple plants from the same Plant class, each with its own **name** and **height**, but sharing the same behavior like **grow**. 

### What You Learn:
- Python program structure and execution flow  
- Organizing complex data structures (lists, dicts, etc.)  
- Writing reusable code with functions and classes  
- Object-Oriented Programming basics: classes, methods, encapsulation  
- Using docstrings and type hints for clarity  
- Implementing scalable and extendable software design
- Enduring pain

> 💡 Think of this module as building your garden management system. Your code becomes a flexible, growing ecosystem.

---

## Module 02 : Garden Guardian Data Engineering for Smart Agriculture

**Theme:** Agricultural Data Pipelines  
**Focus:** Data validation, fault tolerance, and pipeline engineering  

Module 02 primarily focuses on error handling in Python. You are authorized to use **try**, **except**, **raise**, and **finally** along with basic **Exception** types. Basically, a **try** block contains code that may raise an Exception. If an exception occurs, execution immediately stops inside the try block. The **except** block is where you handle the exception, defining how your program should respond to errors. **Raise** allows you to manually trigger an exception when a specific condition is met, and the **finally** block will always execute, regardless of whether an exception occurred or not, which is useful for cleanup actions. **Exception** is the base class for all Python errors. You can create custom exceptions by inheriting from it, allowing you to handle specific error scenarios relevant to your program. Here's an example:
```python
def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except Exception as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")
```
In this example, the function iterates through plant_list and waters each plant. If a *None* value is encountered in the list, it **raises** an exception with a message indicating the plant is invalid. The **except** block catches this exception and prints the error. Regardless of whether an error occurs, the **finally** block executes to close the watering system, ensuring proper cleanup.

### What You Learn:
- Validating and cleaning IoT sensor data streams  
- Handling failure modes in real-time systems  
- Creating custom alerts for specific crop monitoring  
- Building fault-tolerant, robust data pipelines  
- Maintaining data integrity across distributed systems  
- Using exceptions for error handling and graceful program behavior
- Enduring more pain

> 💡 This module teaches you how to be a guardian of data, ensuring that your smart garden system runs smoothly under real-world conditions.  

---

## Module 03 : Data Quest The Pixel Dimension

**Theme:** Game Analytics & Data Structures  
**Focus:** Advanced collection usage  

yeah i give up writing bro it's 5 am and like nobody is reading ts anyway

### What You Learn:
- Command-line communication and input parsing  
- Mastering lists, tuples, sets, and dictionaries  
- Using generators for efficient data processing  
- Comprehensions for data transformation  
- Applying practical data engineering patterns  
- Avoiding file I/O; processing everything in-memory
- Enduring more more pain

> 💡 Level up like an RPG character! Each exercise unlocks a new data superpower, from analyzing scores to processing infinite streams.  

---

## Module 04 : Cyber Archives Training Program

**Theme:** Digital Preservation & File Management  
**Focus:** File operations, streams, and secure handling  

### What You Learn:
- Secure reading and writing of files  
- Stream management using input, output, and alert channels  
- Context managers (`with` statements) for resource safety  
- Exception handling for corrupted archives and access failures  
- Preserving data integrity in all operations
- How to type faster (Me and Andrew finished it in like 20 minutes lol)

> 💡 This module makes you a data archivist. Every file is precious, and every operation must be flawless-like digital archaeology.

---

## Module 05 : Nexus Stream Engineer Training

**Theme:** Polymorphic Data Streams  
**Focus:** Object-oriented design, inheritance, and stream processing  

### What You Learn:
- Method overriding and subtype polymorphism  
- Creating classes with shared interfaces but unique behaviors  
- Designing adaptive and evolving data streams  
- Exception handling to prevent stream corruption  
- Comprehensive type annotations with the `typing` module  
- Building multi-stream systems that interact seamlessly
- Never trust the examples for the exercises because it resulted in me having over 50 lines oF JUST PRINTING LIKE YEAH POLYMORPHISM SICK OK BUT DID 1/3RD OF MY FILES HAVE TO BE PRINT PRINT PRINT

> 💡 This module turns you into a stream engineer in the digital matrix. You learn to think in adaptive, living systems rather than rigid code.

---

## Instructions

### Requirements:
- Python 3.10 or above  
- flake8 for linting: `pip install flake8`  

### How to Run:
- Navigate to the exercise directory  
- Run any Python file using:  
  ```bash
  python3.10 filename.py
  ```  
- Ensure all exercises pass without errors before submission  
- Follow module-specific instructions for testing or helper tools  

---

## Use of AI

During this journey, ChatGPT & Gemini helped:  
- Debug tricky Python errors and understand error messages  
- Transfer smoothly from C syntax to Python syntax  
- Understand Python concepts like OOP, exceptions, and data structures  
- Organize exercises into a cohesive workflow and README structure  

> 💡 Using AI as a guide helped accelerate learning and troubleshoot problems in real-time, making the transition from beginner to... well less beginner, smoother.

---

## Skills Gained Summary

| Module | Key Skills & Concepts |
|--------|---------------------|
| 00 - Python Fundamentals | Basic syntax, functions, I/O, loops, conditionals, code style, optional type hints |
| 01 - Code Cultivation | Program structure, OOP basics, classes & methods, reusable code, docstrings, type hints |
| 02 - Garden Guardian | Data validation, fault tolerance, custom alerts, pipeline design, exception handling |
| 03 - Data Quest | Advanced collections (lists, tuples, sets, dicts), generators, comprehensions, in-memory data processing |
| 04 - Cyber Archives | File operations, secure stream management, context managers, error handling, data preservation |
| 05 - Nexus | Polymorphism, inheritance, method overriding, multi-stream systems, adaptive object-oriented design, type annotations |

> 💡 By completing these modules, you progress from a Python beginner to a skilled engineer capable of handling real-world programming, data pipelines, and complex object-oriented systems.
