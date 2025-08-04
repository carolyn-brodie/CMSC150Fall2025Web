class NoConstructorExample:
    """No Constructor Example"""

    def set_variable(self, value):
        self.x = value

    def __str__(self):
        return f"Object of class that has no constructor but {self.x}"


def tester():
    my_object = NoConstructorExample()
    my_object.set_variable(5)
    print(my_object)



if __name__ == "__main__":
    tester()