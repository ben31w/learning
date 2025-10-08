"""
A massive glossary of Python terms. When you run this program, it prints all the
terms sorted by category and alphabetical order.

The terms are organized into four categories:
- exceptions
- functions
- packages and modules
- terms (about Python and programming)
"""

# Some useful commands:
pip_install_command = 'python3 -m pip install SomePackage'
pip_upgrade_command = 'python3 -m pip install --upgrade pip'
venv_create_command = 'python3 -m venv /path/to/new/virtual/environment'
venv_activate_command = 'source env_name/bin/activate'
venv_deactivate_command = 'deactivate'

exceptions = {
    'SyntaxError': "occurs when Python doesn't recognize a section of a "
        "program as valid Python code.",
    'IndentationError': "occurs when the lines of the program are not properly "
        "indented.",
    'IndexError': "occurs when Python can't find an item at a specified index.",
    'KeyError': "occurs when Python can't find a specified dictionary key.",
    'FileNotFoundError': "occurs when Python can't find the file it's trying "
        "to open.",
    'ZeroDivisionError': "occurs when Python tries to divide a number by zero.",
    'ValueError': "occurs when an operation or function is applied to an "
        "object with an inappropriate value (but still the right type).",
    'TypeError': "occurs when an operation or function is applied to an "
        "object of inappropriate type.",
    'NameError': "occurs when the program tries to use a variable that does "
        "not exist.",
}
functions = {
    'len()': "given an object, returns its length.",
    'sort()': "sorts and permanently changes the order of a list.",
    'sorted()': "given a list as an argument, returns a copy of the list "
        "sorted in a specific order (defaults to ascending, can be changed to "
        "descending by setting the optional 'reverse' parameter to False).",
    '__init__()': "a special Python method that is automatically called when a "
        "class in instantiated. The method defines the class's attributes and "
        "returns an instance of the class.",
    'super()': "allows a subclass to call a method from its superclass.",
    'open()': "opens a given file and returns it as a file object. The only "
        "required parameter for open() is a file name/path. Optional "
        "parameters include mode (files can be opened in read[r]-, write[w]-, "
        "or append[a]-mode), buffering, encoding, errors, newline, closefd, "
        "and opener.",
    'unittest.setUp()': "allows you to create objects that can be reused "
        "across all unit tests when defined in a class that extends "
        "unittest.TestCase.",
    'enumerate()': "given a list as an argument, returns the index and value "
        "of each item.",
    'next()': "given an iterable object, returns the next item in the iterator.",
}

"""

    replace(old, new) -- Returns a copy of the string with all occurrences of the substring old replaced by the string new. The old and new arguments may be string variables or string literals.
    replace(old, new, count) -- Same as above, except only replaces the first count occurrences of old.


    find(x) -- Returns the index of the first occurrence of item x in the string, else returns -1. x may be a string variable or string literal. Recall that in a string, the index of the first character is 0, not 1. If my_str is 'Boo Hoo!':
        my_str.find('!')  # Returns 7
        my_str.find('Boo')  # Returns 0
        my_str.find('oo')  # Returns 1 (first occurrence only)
    find(x, start) -- Same as find(x), but begins the search at index start:
        my_str.find('oo', 2)  # Returns 5
    find(x, start, end) -- Same as find(x, start), but stops the search at index end - 1:
        my_str.find('oo', 2, 4)  # Returns -1 (not found)
    rfind(x) -- Same as find(x) but searches the string in reverse, returning the last occurrence in the string.

count(x) -- Returns the number of times x occurs in the string.


    isalnum() -- Returns True if all characters in the string are lowercase or uppercase letters, or the numbers 0-9.
    isdigit() -- Returns True if all characters are the numbers 0-9.
    islower() -- Returns True if all cased characters are lowercase letters.
    isupper() -- Return True if all cased characters are uppercase letters.
    isspace() -- Return True if all characters are whitespace.
    startswith(x) -- Return True if the string starts with x.
    endswith(x) -- Return True if the string ends with x.


    capitalize() -- Returns a copy of the string with the first character capitalized and the rest lowercased.
    lower() -- Returns a copy of the string with all characters lowercased.
    upper() -- Returns a copy of the string with all characters uppercased.
    strip() -- Returns a copy of the string with leading and trailing whitespace removed.
    title() -- Returns a copy of the string as a title, with first letters of words capitalized.

split() splits a string into a list of tokens. Each token is a substring that forms a part of a larger string. A separator is a character or sequence of characters that indicates where to split the string into tokens. 

join() string method performs the inverse operation of split() by joining a list of strings together to create a single string.



list() function accepts a single iterable object argument, such as a string, list, or tuple, and returns a new list object. 



"""

modules_and_packages = {
    'json': "a standard Python module that allows you to load and dump data "
        "into JSON (JavaScript Object Notation) files. The JSON data format is "
        "used across many different programming languages. The json module is "
        "useful for storing and saving user-generated data when a program "
        "runs, and reloading that same data after the program has stopped "
        "running.",
    'unittest': "a standard Python module with tools for testing code via unit "
        "tests. To use unit tests, you must create a class that extends the "
        "unittest.TestCase class. Any method inside the class that starts with "
        "'test_' acts as a unit test, and these methods are automatically "
        "called when the line 'unittest.main()' is called. unittest contains "
        "methods that allow you to verify if a class or function works as "
        "intended, such as assertEqual(a, b), assertNotEqual(a, b), "
        "assertTrue(x), assertFalse(x), assertIn(item, list), and "
        "assertNotIn(item, list).",
    'pip': "a module that acts as a package management system, allowing users "
        "to download, install, and manage Python packages. More modern "
        "versions of Python come with pip preinstalled. To use pip to install "
        "the latest version of a package from the Python Package Index (PyPI), "
        f"enter this command: {pip_install_command}",
    'sys': "a standard Python module containing functions and variables used "
        "to manipulate different parts of the Python runtime environment. FUN "
        "FACT: sys was originally written in C.",
    'os': "a standard Python module containing operating system informational "
        "and management helpers ",
    'time': "a standard Python module with time-related functions. Can get the "
        "current time, convert timezones, and sleep for a number of seconds.",
    'pygame': "a free, open-source Python library for making multimedia "
        "applications like games. It contains helpful tools to manage the "
        "graphics, animations, and sounds of a video game project.",
    'numpy': "a library for Python that adds support for large, multi-"
        "dimensional arrays and matrices, along with a large collection of "
        "high-level mathematical functions to operate on these arrays.",
    'matplotlib': "a mathematical plotting library for Python and its "
        "numerical mathematics extension NumPy. It provides an object-oriented "
        "API for embedding plots into applications using general-purpose GUI "
        "toolkits like Tkinter, wxPython, Qt, or GTK+. Its packages include "
        "kiwisolver, pyparsing, six, cycler, numpy, python-dateutil, and "
        "matplotlib.",
    'plotly': "a package that contains tools for graphing, analytics, and "
        "statistics. It is capable of producing high-quality, interactive "
        "graphs. It exists in the following languages: Python, R, MATLAB, "
        "Perl, Julia, Arduino, and REST.",
    'csv (module)': "a standard Python module with classes and methods to "
        "perform read-and-write operations on CSV (comma-separated values) "
        "files.",
    'datetime': "a standard Python module with date- and time-related classes "
        "and functions.",
    'requests': "a package that allows a Python program to easily request info "
        "from a website and examine the response.",
    'venv': "a standard Python module that provides support for creating "
        "virtual environments. To create a virtual environment inside a "
        f"directory, enter this command: '{venv_create_command}'. To activate "
        "the virtual environment, navigate to its parent directory and enter "
        f"this command: '{venv_activate_command}'. To deactivate it, enter "
        f"'{venv_deactivate_command}.' Packages installed in the virtual "
        "environment are only available while the environment is active.",
    'django': "a Python-based, free, open-source web framework. In Django, "
        "every web app you want to create is called a project, and a project "
        "is a sum of applications. An application is a set of code files "
        "relying on the MVT pattern. When building a website using Django, the "
        "website is the project, and the forum, news, and contact engine are "
        "applications.",
    'copies': "a standard Python module that can create complete copies of objects.",
    'pbd': "the Python interactive debugger.",
    'urllib': "a standard Python module with URL handling functions, such as "
        "requesting web pages.",
}
terms = {
    'function': "a named block of code designed to do one specific job. "
        "Functions are always followed by a set of parentheses when called.",
    'method': "a function that is part of a class. Methods are always defined "
        "using 'self' as the first parameter, but 'self' is never explicitly "
        "initialized when the method is called.",
    'string': "a series of characters. In Python, strings can be written "
        "inside single('') or double quotes(\"\").",
    'whitespace': "any non-printing character, such as spaces, tabs, and end-"
        "of-line symbols.",
    'list': "a collection of items in a particular order. Defined using square "
        "brackets ( [] ).",
    'immutable': "unable to be changed.",
    'tuple': "an immutable list defined using parentheses ( () ).",
    'conditional test': "an expression that evaluates to either True or False.",
    'dictionary': "a collection of items that stores data in key:value pairs. "
        "Defined using curly braces ( {} ).",
    'docstring': "an unassigned, multi-line string enclosed in triple quotes"
        "(\"\"\"\"\"\"). Docstrings are similar to comments, and their purpose "
        "is to document what a module, function, class, method, or other "
        "segment of code does (they are usually the first lines written when "
        "defining a module, function, etc.).",
    'parameter': "a piece of information a function needs to do its job.",
    'argument': "a piece of information passed from a function call to a "
        "function. Arguments are written inside the parentheses of a function "
        "when it is called. There are two types of arguments: keyword (e.g., "
        "paramater_name=value) and positional (e.g., value).",
    '*args': "a generic parameter for collecting an arbitrary number of "
        "positional arguments. In Python syntax, any parameter with a single "
        "leading asterisk is initialized as a tuple. The tuple contains any "
        "arguments in the function call that follow the function's required "
        "arguments.",
    '**kwargs': "a generic parameter for collecting an arbitrary number of "
        "keyword arguments. In Python syntax, any parameter with two leading "
        "asterisks is initialized as a dictionary. The dictionary takes "
        "keyword arguments in the function call that follow the function's "
        "required arguments and stores them as key:value pairs.",
    'module': "a file of Python code that can be imported and reused in other "
        "program files. Any Python file is technically a module.",
    'package': "a collection of modules; specifically, a directory containing "
        "various Python files and a '__init__.py' file. Python treats imported "
        "packages the same as imported modules (both module objects), so when "
        "you import a package on its own, the only classes, variables, and "
        "methods you can use are those inside the __init__.py file. To use "
        "classes and methods that are in the package but not in the "
        "__init__.py file, you must import them.",
    'class': "a program that consists of functions and data to represent a "
        "real-world thing.",
    'instantiation': "the act of creating an object or instance of a class.",
    'attribute': "a variable inside a class that can be accessed by an "
        "instance of the class. Attributes are defined using the prefix "
        "'self.'",
    'inheritance': "when one class (known as a child class or subclass) "
        "receives and extends the attributes, methods, etc. of another class "
        "(known as a parent class or superclass).",
    'Python standard library': "a set of modules included with every Python "
        "installation. To use these modules in a program, you must import "
        "them. When you import modules from the standard library, you should "
        "place their import statements above any import statements for modules "
        "you wrote, and put a blank line between them.",
    'with': "a Python keyword which, when paired with open(), allows you to "
        "open a file and automatically close it once all the code inside the "
        "with block is executed.",
    'exception': "an object created by Python whenever a run-time error "
        "occurs within a program. If your code is written to handle the "
        "exception, the program will continue to run. Otherwise, the program "
        "will halt and show a traceback, which includes a report of the "
        "exception raised. When you think an error may occur, you can write a"
        "try-except block to handle the exception that might be raised.",
    'refactoring': "the process of breaking up code into a series of functions "
        "that have specific jobs.",
    'unit test': "a test to verify that one specific aspect of a function's "
        "behavior is correct. Unit tests can be run by importing the unittest "
        "module from the Python standard library.",
    'test case': "a collection of unit tests that together prove that a "
        "function behaves as it's supposed to, within the full range of "
        "situations you expect it to handle. A perfect test case has full "
        "coverage, meaing it includes a full range of unit tests covering all "
        "the possible ways you can use a function. Full coverage is hard to "
        "achieve on large projects, so many test cases simply test the code's "
        "critical behaviors.",
    'version control': "software that allows you to create 'snapshots' or "
        "'save states' of a project whenever it's in a working state. If you "
        "make changes to a project, version control allows you revert back to "
        "a previous working state if the current state isn't functioning well."
        "Git is the most popular version control software.",
    'helper method': "a method that is reused often inside other methods or "
        "parts of a program. Helper methods can be written inside a class, but "
        "they aren't meant to be called through an instance of the class. In "
        "Python, a single leading underscore indicates a helper method.",
    'floor division': "division that produces an integer quotient instead of a "
        "float. Floor division drops any remainder after the decimal point, "
        "but it does NOT round the answer. In Python, floor division is "
        "indicated by double slashes (//).",
    'data analysis': "the process of using code to explore the patterns and "
        "connections in a data set.",
    'data visualization': "the graphic representation of data. Data analysis "
        "is often used to create data visualizations.",
    'API': "(application programming interface) an interface with a set of "
        "instructions that allow programmers to access specific features or "
        "data of an application, operating system, or other service.",
    'web framework': "a set of tools designed to help build interactice "
        "websites.",
    'spec': "short for specification, a piece of writing that describes a "
        "project. A full spec details the project goals, describes the "
        "project's functionality, and discusses its appearance and user "
        "interface.",
    'virtual environment': "a place on your system where you can install "
        "packages and isolate them from all other Python packages.",
    'localhost': "a server that only processes requests on your system.",
}

# Print the terms sorted by category and alphabetical order.
print("-------------------exceptions-------------------\n")
for exception, description in sorted(exceptions.items()):
    print(f"{exception}: {description}\n")

print("-------------------functions-------------------\n")
for function, description in sorted(functions.items()):
    print(f"{function}: {description}\n")

print("-------------------modules and packages-------------------\n")
for mp, defintion in sorted(modules_and_packages.items()):
    print(f"{mp}: {defintion}\n")

print("-------------------terms-------------------\n")
for term, definition in sorted(terms.items()):
    print(f"{term}: {definition}\n")