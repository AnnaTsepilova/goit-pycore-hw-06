import re
from field import Field

class Phone(Field):
    def __init__(self, number):
        self.value = self.validate(number)

    def validate(self, number):
        ''' Simple phone number validation '''
        if not re.match(r"^\+?(\d{10})$", number.strip()):
            pass

        return number
