class Name:
    def __init__(self, name=""):
        names = name.split() # returns a list of all the names
        self.count = len(names)
        self.first = ''
        self.middle = ''
        self.last = ''
        self.suffix = ''

        if self.count == 1:
            self.first = names[0]
        elif self.count == 2:
            self.first = names[0]
            self.last = names[1]
        elif self.count >= 3:
            self.first = names[0]
            self.middle = names[1]
            self.last = names[2]
            if self.count == 4:
                self.suffix = names[3]

    def get_first(self):
        return self.first

    def get_middle(self):
        return self.middle

    def get_last(self):
        return self.last

    def get_suffix(self):
        return self.suffix

    def set_first(self, value):
        if value == '' and self.first != '':
            self.count -= 1
        elif self.first == '':
            self.count += 1
        self.first = value

    def set_middle(self, value):
        if value == '' and self.middle != '':
            self.count -= 1
        elif self.middle == '':
            self.count += 1
        self.middle = value

    def set_last(self, value):
        if value == '' and self.last != '':
            self.count -= 1
        elif self.last == '':
            self.count += 1
        self.last = value

    def set_suffix(self, value):
        if value == '' and self.suffix != '':
            self.count -= 1
        elif self.suffix == '':
            self.count += 1
        self.suffix = value

    def get_count(self):
        return self.count

    def get_name(self):
        name = ''
        if self.first != '':
            name += self.first + ' '
        if self.middle != '':
            name += self.middle + ' '
        if self.last != '':
            name += self.last + ' '
        if self.suffix != '':
            name += self.suffix
        if name[len(name)-1] == ' ':
            name = name[:len(name)-1]
        return name

    def get_initials(self):
        initials = ''
        if self.first != '':
            initials += self.first[0]
        if self.middle != '':
            initials += self.middle[0]
        if self.last != '':
            initials += self.last[0]
        return initials
