filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in contents:
            print(line.rstrip())