class DebitCard:

    def __init__(self, customer, bank, acnt):

        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._balance = 0

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if self._balance - price < 0:
            return False
        else:
            self._balance = self._balance - price

    def receive(self, amount):
        self._balance = self._balance + amount
        return self._balance

    def __str__(self):
        return ' '.join([self._customer, self._bank, str(self._account), str(self._balance)])


if __name__ == "__main__":
    kartica = DebitCard("Pera Peric", "ABC", "123-456")
    print(kartica)
