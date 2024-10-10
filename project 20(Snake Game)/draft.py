class Animal:
    def __init__(self):
        self.eyes=2

    def breath(self):
        print("inhale and exhale")

class Cat(Animal):
    def __init__(self):
        super().__init__()
    def breath(self):
        super().breath()
        print("and runn")

twi=Cat()
twi.breath()
