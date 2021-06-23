class Position:
    sequence = 0
    def __init__(self, des='Sin cargo'):
        Position.sequence += 1
        self.code = Position.sequence
        self.description = des


if __name__ == '__main__':
    position1 = Position()
    print(position1.code, position1.description)
    position2 = Position()
    position2.description='Director'
    print(position2.code, position2.description)
    position3 = Position('Analista')
    print(position3.code, position3.description)
