class Position:
    sequence = 0
    def __init__(self, des='Sin cargo'):
        Position.sequence += 1
        self.code = Position.sequence
        self.description = des
