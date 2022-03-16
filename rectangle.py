class Rectangle(object):

    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b

    def __str__(self):
        return "Pravouganik ima prvu stranicu " + str(self._a) + " i drugu " + str(self._b)

    def obim(self):
        return "Obim iznosi " + str(2 * self._a + 2 * self._b)

    def povrsina(self):
        return "Povrsina iznosi " + str(self._a * self._b)


class Square(Rectangle):

    def __init__(self, a):
        self._a = a
        self._b = a


if __name__ == "__main__":
    pravouganik = Rectangle(2, 5)
    print(pravouganik)
    print(pravouganik.obim())
    print(pravouganik.povrsina())

    kvadrat = Square(2)
    print(kvadrat.povrsina())
