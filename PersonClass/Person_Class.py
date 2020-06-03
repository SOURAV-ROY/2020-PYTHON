def method_name():
    print('Sourav Roy')


class Person:
    def __init__(self, person_name: str, date_of_year: int, ht_inches: int = None):
        # Private Variable In Python ********************
        self.__name = person_name
        self.__date_of_birth = date_of_year
        self.__height = ht_inches
        # Public Variable in Python *********************
        self.look = None

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if self._has_any_number(new_name):
            print("Sorry Person Can't have any number")
            return
        self.__name = new_name

    def _has_any_number(self, string):
        return "0" in string

    def get_summery(self):
        return f"Name: {self.__name}, DOB: {self.__date_of_birth}, Height: {self.__height}"


method_name()
person_summery = Person("First Person", 1994, 70)
print(person_summery.get_summery())
print(person_summery.look)

person_summery.set_name("Sourav Chandra Roy")
print(person_summery.get_summery())

person_summery.set_name('111100000111Sourav')
print(person_summery.get_summery())
