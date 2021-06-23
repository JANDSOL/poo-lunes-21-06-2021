from position import Position

class Employee:
    sequence = 0

    def __init__(self, nam, ica, sal, pos):
        self.id = self.generate_code()
        self.name = nam
        self.identity_card = ica
        self.salary = sal
        self.position = pos

    def generate_code(self):
        Employee.sequence += 1
        return Employee.sequence
