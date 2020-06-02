def method_name():
    print('Sourav Roy')


class Person:
    def __init__(self, person_name, date_of_birth, ht):
        self.name = person_name
        self.date_of_birth = date_of_birth
        self.height = ht

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_summery(self):
        return f"Name: {self.name}, DOB: {self.date_of_birth}, Height: {self.height}"


method_name()
person_summery = Person("First Person", "1996", "6 feet")
print(person_summery.get_summery())
person_summery.set_name("Sourav Chandra Roy")
print(person_summery.get_summery())
