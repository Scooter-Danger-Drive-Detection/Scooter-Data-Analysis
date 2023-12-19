from models import Frame


class FrameBatch:
    def __init__(self, frames: list[Frame]):
        self.batch_size = len(frames)

        self.average_speed = sum(frame.gps.speed for frame in frames) / len(frames)
        self.min_speed = min(frame.gps.speed for frame in frames)
        self.max_speed = max(frame.gps.speed for frame in frames)

        self.average_acceleration = sum(frame.accelerometer.total_acceleration for frame in frames) / len(frames)
        self.min_acceleration = min(frame.accelerometer.total_acceleration for frame in frames)
        self.max_acceleration = max(frame.accelerometer.total_acceleration for frame in frames)

        self.average_angle_speed = sum(frame.gyroscope.total_angle_speed for frame in frames) / len(frames)
        self.min_angle_speed = min(frame.gyroscope.total_angle_speed for frame in frames)
        self.max_angle_speed = max(frame.gyroscope.total_angle_speed for frame in frames)

        self.time_delta = max(frame.time for frame in frames) - min(frame.time for frame in frames)
