from models import Frame, Session, SafeRideMode


class FrameBatch:
    def __init__(self, frames: list[Frame], session: Session):
        self._batch_size = len(frames)

        not_null_speeds = [frame.gps.speed for frame in frames if frame.gps.speed != 0]
        if len(not_null_speeds) == 0:
            self.average_speed = 0
            self.min_speed = 0
            self.max_speed = 0
        else:
            self.average_speed = sum(not_null_speeds) / len(not_null_speeds)
            self.min_speed = min(not_null_speeds)
            self.max_speed = max(not_null_speeds)

        self.average_acceleration = sum(frame.accelerometer.total_acceleration for frame in frames) / len(frames)
        self.min_acceleration = min(frame.accelerometer.total_acceleration for frame in frames)
        self.max_acceleration = max(frame.accelerometer.total_acceleration for frame in frames)

        self.average_angle_speed = sum(frame.gyroscope.total_angle_speed for frame in frames) / len(frames)
        self.min_angle_speed = min(frame.gyroscope.total_angle_speed for frame in frames)
        self.max_angle_speed = max(frame.gyroscope.total_angle_speed for frame in frames)

        self.time_delta = max(frame.time for frame in frames) - min(frame.time for frame in frames)

        self.ride_mode = 0 if isinstance(session.ride_mode, SafeRideMode) else 1
