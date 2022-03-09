from multiprocessing.sharedctypes import Value


class DebitCard:

    def __init__(self, customer, account_number, bank):

        self._customer = customer
        self._account_number = account_number
        self._bank = bank
        self._balance = 0

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, cust):
        self._customer = cust

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, number):
        self._account_number = number

    @property
    def bank(self):
        return self._bank

    @bank.setter
    def bank(self, bank):
        self._bank = bank

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def receive(self, amount):
        if amount < 0:
            return False
        self._balance = self._balance + amount
        return True

    def charge(self, amount):
        if self._balance - amount < 0:
            raise ValueError("Nedozvoljena vrednost!")
        else:
            self._balance = self._balance - amount

    def __str__(self):
        return ' '.join([self._customer, self._account_number, self._bank, str(self._balance)])


if __name__ == "__main__":
    kartica = DebitCard("Pera Peric", "123-456", "ABC Banka")
    print(kartica)
    kartica.receive(1000)
    print("Nakon uplate na racun: ", kartica)
    try:
        kartica.charge(-100)
    except ValueError:
        print("Desila se greska")
