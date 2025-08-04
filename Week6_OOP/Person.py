class Person:
#
    # Constructor
    def __init__(self, name, ssn, phone):
        self.name = name
        self.ssn = ssn
        self.phone_number = phone

    # Other Methods
    def change_phone_number(self, new_number):
        self.phone_number = new_number

    # Print Method
    def __str__(self):
        out = f"{self.name} has ssn {self.ssn} and phone number {self.phone_number}"
        return out
#
def tester():
    joel = Person("Joel", "4444-44-4444", "111-123-3456")
    print(joel)
    joel.change_phone_number("555-555-5555")
    print(joel)

if __name__ == "__main__":
    tester()

