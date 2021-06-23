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


if __name__ == '__main__':
    position1 = Position('Docente')
    employee1 = Employee('Daniel', '0914', 500, position1)
    employee1.show()

    position2 = Position('Analista')
    employee2 = Employee('Ana', '0914', 500, position2)
    employee2.show()
    