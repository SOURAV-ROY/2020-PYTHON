def method_name():
    print('Sourav Roy')


class Person:
    def __init__(self, person_name: str, year_of_birth: int, ht_inches: int = None):
        # Private Variable In Python ********************
        self.__name = person_name
        self.__date_of_birth = year_of_birth
        self.__height = ht_inches
        # Public Variable in Python *********************
        self.look = None

    def get_year_of_birth(self):
        return self.__date_of_birth

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
        return f"Name: {self.__name}, " \
               f"DOB: {self.__date_of_birth}, " \
               f"Height: {self.__height if self.__height is not None else '**Invalid**'} "


# method_name()
# person_summery = Person("First Person", 1994, 70)
# print(person_summery.get_summery())
# print(person_summery.look)
#
# person_summery.set_name("Sourav Chandra Roy")
# print(person_summery.get_summery())
#
# person_summery.set_name('111100000111Sourav')
# print(person_summery.get_summery())

person_list = [Person("First Person", 1992, 70),
               Person("Sourav", 1993, 72),
               Person("Roy", 1995),
               Person("First ", 1996, 50),
               Person("Second", 1997),
               Person("Third", 1998),
               Person("Fourth", 1991, 80),
               Person("Fifth", 1971, 75),
               Person("Sixth", 2020, 75)]

for person in person_list:
    # if person.get_year_of_birth() is not None and person.get_year_of_birth() >= 1995:
    if person.get_year_of_birth() >= 1995:
        print(person.get_summery())
