class Student(object):

    def __init__(self, name, surname):
        self._name = name
        self._surname = surname
        ocene = []

    @property
    def name(self):
        return self._name

    @name.setter
    def
