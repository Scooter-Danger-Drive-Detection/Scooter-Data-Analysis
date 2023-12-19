class RideMode:
    key = -1


class SafeRideMode(RideMode):
    def __init__(self):
        super(SafeRideMode, self).__init__()
        self.key = 0


class UnsafeRideMode(RideMode):
    def __init__(self, alone: bool):
        super(UnsafeRideMode, self).__init__()
        self.alone = alone
        if alone:
            self.key = 1
        else:
            self.key = 2


class TestRideMode(RideMode):
    def __init__(self):
        super(TestRideMode, self).__init__()
        self.key = 3


def get_ride_mode_by_key(key: int):
    ride_modes = {
        0: SafeRideMode(),
        1: UnsafeRideMode(alone=True),
        2: UnsafeRideMode(alone=False),
        3: TestRideMode(),
    }
    return ride_modes[key]
