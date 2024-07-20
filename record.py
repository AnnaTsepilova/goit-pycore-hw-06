from phone import Phone
from name import Name

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number) -> None:
        '''Function add phone number to record'''
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        '''Function removes phone number from record'''
        pass

    def edit_phone(self, old_number, new_number):
        pass

    def find_phone(self, number):
        '''Search phone in record'''
        result = [n.value for n in self.phones if number == n.value]
        if result:
            return result[0]

        return False

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
