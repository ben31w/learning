# Python is great at analyzing data. It is used for data-intensive work in 
#  genetics, climate research, political and economic analysis, etc.
glossary = {
    'data visualization': "the graphic representation of data. Data "
        "visualization is closely associated with data analysis.",
    'data analysis': "the process of using code to explore the patterns and "
        "connections in a data set.",
    'Matplotlib': "a mathematical plotting library for Python and its "
        "numerical mathematics extension NumPy. It provides an object-oriented "
        "API for embedding plots into applications using general-purpose GUI "
        "toolkits like Tkinter, wxPython, Qt, or GTK+. Its packages include "
        "kiwisolver, pyparsing, six, cycler, numpy, python-dateutil, and "
        "matplotlib.",
    'Plotly': "a package that contains tools for graphing, analytics, and "
        "statistics. It is capable of producing high-quality, interactive "
        "graphs. It exists in the following languages: Python, R, MATLAB, "
        "Perl, Julia, Arduino, and REST.",
    'colormap': "a series of colors in a gradient that moves from a starting "
        "to an ending color.",
    'csv (module)': "a Python standard libary module with classes and methods "
        "to perform read-and-write operations on CSV (comma-separated values) "
        "files.",
    'API': "(application programming interface) an interface with a set of "
        "instructions that allow programmers to access specific features or "
        "data of an application, operating system, or other service.",
    'Requests': "a package that allows a Python program to easily request info "
        "from a website and examine the response.",
}

for term, definition in sorted(glossary.items()):
    print(f"{term}: {definition}\n")