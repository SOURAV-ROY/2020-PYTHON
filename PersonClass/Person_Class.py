def method_name():
    print('Sourav Roy')


def _has_any_number(string):
    return "0" in string


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
        if _has_any_number(new_name):
            print("Sorry Person Can't have any number")
            return
        self.__name = new_name

    def get_summary(self):
        pass
        # return f"Name: {self.__name}, " \
        #        f"DOB: {self.__date_of_birth}, " \
        #        f"Height: {self.__height if self.__height is not None else '**Invalid**'} "


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


# for person in person_list:
#     # if person.get_year_of_birth() is not None and person.get_year_of_birth() >= 1995:
#     if person.get_year_of_birth() >= 1995:
#         print(person.get_summary())


class Student(Person):
    def __init__(self, person_name: str, year_of_birth: int, student_id: str, email_id: str):
        super().__init__(person_name, year_of_birth)
        self.email = email_id
        self.id = student_id

    def get_summary(self):
        # return f'Name: {self.get_name()}, ID: {self.id}, Email: {self.email}, Birth: {self.get_year_of_birth()}'
        return f"Name: {self.get_name()}, ID: {self.id} Email: {str(self.email)}, Birth: {self.get_year_of_birth()}"

    def __str__(self):
        return self.get_summary()
        # return f"Name: {self.get_name()}, ID: {self.id} Email: {self.email}, Birth: {self.get_year_of_birth()}"

    def __repr__(self):
        return self.get_summary()
        # return f"Name: {self.get_name()}, ID: {self.id} Email: {self.email}, Birth: {self.get_year_of_birth()}"


student_summary = Student("Pangku", 2000, '456abc123', "pangku@gmail.com")
# print(student_summery.get_summary())
print(student_summary)
student_summary.set_name("Sourav Roy")
# print(student_summery.get_summary())
print(student_summary)


class Teacher(Person):
    def __init__(self, person_name: str, year_of_birth: int, department: str):
        super().__init__(person_name, year_of_birth)
        self.dept = department

    def get_summary(self):
        return f'{self.get_name()} Is A Teacher'


new_person_list = [
    Person("Pangku", 2000),
    Student("Sourav RoyRoy", 1994, '456abc123', "souravroy@gmail.com"),
    Teacher("Gaurab Roy", 1980, "CSE")
]

for p in new_person_list:
    # print(p.get_name())
    print(p.get_summary())


class WoWClass:
    pass


plainClass = WoWClass()
plainClass.age = 22
plainClass.movie = "Movie"
print(plainClass.movie)
print(plainClass.age)
