class ComplexNumber(object):

    def __init__(self, real, imaginary):
        self._imaginary = imaginary
        self._real = real

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, real):
        self._real = real

    @property
    def imaginary(self):
        return self._imaginary

    @imaginary.setter
    def imaginary(self, imaginary):
        self._imaginary = imaginary

    def __str__(self):
        return str(self._real) + "+" + str(self._imaginary) + "i"

    def __add__(self, complex):
        real_part = self._real
        imaginary_part = self._imaginary
        real_complex = complex.real
        imaginary_complex = complex.imaginary

        return ComplexNumber(real_part + real_complex, imaginary_part + imaginary_complex)

    def __sub__(self, complex):
        real_part = self._real
        imaginary_part = self._imaginary
        real_complex = complex.real
        imaginary_complex = complex.imaginary

        return ComplexNumber(real_part - real_complex, imaginary_part - imaginary_complex)


if __name__ == "__main__":
    n1 = ComplexNumber(2, 4)
    n2 = ComplexNumber(3, 4)
    print(n1+n2)
    print(n1-n2)
