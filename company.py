class Person:
    def __init__(self,name,surname):
        self._name = name
        self._surname = surname
    
    @property

    def name(self):
        return self._name
    
    @name.setter

    def name(self,name):
        self.name = name
    
    @property

    def surname(self):
        return self._surname
    
    @surname.setter

    def surname(self,surname):
        self.surname = surname
    
    def __str__(self):
        return "Name: " + self._name + " Surname: " + self._surname

class User(Person):

    def __init__(self,name,surname,username,password):
        super().__init__(name,surname)
        self._username = username
        self._password = password

    @property

    def username(self):
        return self._username
    
    @username.setter

    def username(self,username):
        self._username = username
    
    @property

    def password(self):
        return self._password
    
    @password.setter

    def password(self,password):
        self._password = password

    def __str__(self):
        return "Name: " + self._name + ", surname: " + self._surname + " password: " + self._password + " username: " + self._username


class RegisteredClient(User):

    def __init__(self,name,surname,username,password,phone,mail,gender):
        super().__init__(name,surname,username,password)
        self._phone = phone
        self._mail = mail
        self._gender = gender
        self._role = "Client"

    
    @property

    def phone(self):
        return self._phone
    
    @phone.setter

    def phone(self,phone):
        self._phone = phone
       
    @property

    def mail(self):
        return self._mail
    
    @mail.setter

    def mail(self,mail):
        self._mail = mail
    
    @property

    def gender(self):
        return self._gender
    
    @gender.setter

    def gender(self,gender):
        self._gender = gender
    
    def __str__(self):

           return "Name: " + self._name + ", surname: " + self._surname + " role: " + self._role

class Receptionist(User):
    def __init__(self,name,surname,username,password):
        super().__init__(name,surname,username,password)
        self._role = "Receptionist"

    def __str__(self):
        return "Name: " + self._name + "Surname: " + self._surname + " role: " + self._role


class Beautician(User):

    def __init__(self,name,surname,username,password,treatments=None):
        super().__init__(name,surname,password,username)
        self._role = "Beautician"
        self._treatments = treatments
        if treatments == None:
            treatments = []
        self._treatments = treatments


        @property

        def treatments(self):
            return self._treatments

    def add_treatments(self,treatment):
        treatment.append(treatment)


    def __str__(self):
        return "Name: " + self._name + "surname: " + self._surname + "role: " + self._role

class Manager(User):

    def __init__(self,name,surname,username,password,subordinates=None):
        super().__init__(name,surname,password,username)
        if subordinates == None:
            subordinates = []
        self._subordinates = subordinates


    @property

    def subordinates(self):
        return self._subordinates
    

    def add_subordinates(self,employee):
        self._subordinates.append(employee)
    
    def remove_subordinates(self,employee):
        self._subordinates.remove(employee)

    def __str__(self):
        return "Name: " + self._name + " surname: " + self._surname + " his employees: " + str(self._subordinates)


class Company(object):

    def __init__(self,name,employees,manager):

        self._name = name
        self._manager = manager
        self._employees = employees
        self._employees = []

     
    @property

    def name(self):
        return self._name
    
    @name.setter

    def name(self,name):
        self._name = name

    @property

    def manager(self):
        return self._manager

    @manager.setter

    def manager(self,manager):
        self._manager = manager
    
    def deploy(self,employee,skill):
        if (skill == "Receptionist" or "Beautician"):
            self._employees.append(employee)

        return "Manager has deployeed " + employee 

 

    def __str__(self):
        return "Company's name is " + self._name 
    


if __name__ == "__main__":
    osoba = Person("Pera","Peric")
    print(osoba)
    user = User("Ana","Stevanovic","anna","1234")
    print(user)
    registrovani_klijent = RegisteredClient("Ivica","Dacic","1234","ivvy","ivy@gmail.com","12345","male")
    print(registrovani_klijent)
    recepiconar = Receptionist("Mirko","Mirkovic","mirry","12345")
    print(recepiconar)

    menadzer = Manager("Ana","Micic","qweqwe","31232123")
    menadzer.add_subordinates("Milica")
    menadzer.add_subordinates("Milica2")
    print(menadzer)

    menadzer.remove_subordinates("Milica")
    print(menadzer)

    kompanija = Company("Tarkett","Milica,Perica","Jovan")
    print(kompanija.deploy("Anastasija","Receptionist"))
    print(kompanija)


    