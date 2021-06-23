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

    def show(self):
        print('código:{}, nombre:{}, cargo:{}-{}'.format(self.id, self.name,\
                                                         self.position.code,\
                                                     self.position.description))
