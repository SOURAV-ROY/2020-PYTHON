def method_name():
    print('Sourav Roy')


class Person:
    def __init__(self, person_name):
        self.name = person_name

    def get_name(self):
        return self.name


method_name()
a_person = Person('First Person')
b_person = Person('Second Person')

print(a_person.get_name())
print(b_person.get_name())
