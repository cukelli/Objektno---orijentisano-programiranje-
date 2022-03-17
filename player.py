import abc

class Player(object):

    def __init__(self,health:float,mana:float):
        self._health = health
        self._mana = mana
    
    @property

    def health(self):
        return self._health

    @health.setter

    def health(self,health):
        self._health = health 

       
    @property

    def mana(self):
        return self._mana

    @mana.setter

    def mana(self,mana):
        self._mana = mana 

    def __str__(self):
        return "Player's health is " + str(self._health) + " and mana is " + str(self._mana)


class Item(abc.ABC):

    def __init__(self,value:float):
        self._value = value

    @property

    def value(self):
        return self._value

    @value.setter

    def value(self,value):
        self._value = value

    @abc.abstractmethod
    def use(self,player):
        pass
    

    def __str__(self):
        return "Item's value is " + str(self._value) + "."


class Food(Item):
    
    def __init__(self,value:float):
        super().__init__(value)

    def use(self,player):
        player.health = player.health + self._value

    
    def __str__(self):
        return "Food's value is " + str(self._value) + "."

class Potion(Item):

    def __init__(self,value:float,type:str):
        super().__init__(value)
        self._value = value
        self._type = type

    @property

    def type(self):
        return self._type

    @type.setter

    def type(self,type):
        self._type = type


    def use(self,player):
        if (self._type == "health"):
            player.health = player.health + self._value
        else:
            player.mana = player.mana + self._value
    
    def __str__(self):
        return "Value of this item is " + str(self._value) + "and it's type is " + self._type 


if __name__ == "__main__":

    playerTest = Player(2,5) 
    print(playerTest)
    apple = Food(3)
    print(apple)
    elixir= Potion(3,"health")
    elixir.use(playerTest)
    print(playerTest)
    elixir = Potion(6,"mana")
    elixir.use(playerTest)
    print(playerTest)