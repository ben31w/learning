"""A glossary containing terms about computers and programming."""

# The terms
terms = {
    'switch': "an electronic component or device that controls whether or not "
        "electricity flows through a wire.",
    'circuit': "a connection of switches",
    'bit': "a binary digit that can have one of two values: 0 or 1.",
    'processor': "a circuit that can process/execute a list of desired calculations/instructions.",
    'memory': "a circuit that can store info and instructions (all represented "
        "as bits) in a series of addressed locations.",
    'progam': "a sequence of instructions created by a programmer. AKA an application/app.",
    'machine instructions': "instructions for computers written as 0s and 1s.",
    'executable program': "a sequence of machine instructions.",
    'assembly language': "human-readable processor instructions.",
    'assembler program': "a program that translates assembly language instructions "
        "to machine instructions.",
    'high-level languages': "supports programming using formulas or algorithms.",
    'compiler': "a program that automatically translates high-level language "
        "programs into executable programs.",
    'scripting language': "a programming language that executes programs (called "
        "scripts) without compiling them.",
    'interpreter': "a program that executes scripts.",
    'garbage collection': "when an interpreter automatically deletes unneeded "
        "objects from the memory once they are done being used. Garbage collection "
        "implemented into Python 2.",

}

# Print the terms.
for k, v in sorted(terms.items()):
    print(f"{k}: {v}\n")