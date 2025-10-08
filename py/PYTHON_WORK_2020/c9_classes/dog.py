"""A class that can be used to model a dog. This is my first class in Python."""

class Dog:
    """A simple attempt to model a dog."""

    # self is always the first parameter in the __init__() method.
    #  Although self is always a parameter, self is never passed as an argument
    #  because Python does so automatically whenever the method is called.
    
    # the __init__() method is called whenever an instance of the class (in this
    #  case, Dog) is created/instantiated, and it returns the said instance.

    # Ex: 
    #    my_dog = Dog('Georgia', 8)
    # This line will call the __init__() method in Dog, and it will return a Dog.
    
    def __init__(self, name, age):
        """
        Initialize name and attributes.

        The following lines take the parameters name and age, and associate them
        with variables/attributes called name and age that can be accessed by
        any instance of the Dog class.
        """
        self.name = name
        self.age = age

    
    # All methods in a class contain the self parameter. Just like the 
    #  __init__() method, methods that belong to a class automatically pass self
    #  when they are called, so there's no need to define self as an argument in
    #  the method call.
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")