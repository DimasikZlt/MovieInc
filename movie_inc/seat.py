class Seat:
    def __init__(self, index, is_busy=False):
        self.index: int = index
        self.is_busy: bool = is_busy

    def is_seat_busy(self):
        return self.is_busy

    def take_seat(self):
        self.is_busy = True

    def leave_seat(self):
        self.is_busy = False
