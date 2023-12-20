import math


class Frame:
    class GPS:
        def __init__(self, speed: float, longitude: float, latitude: float):
            self.speed = speed
            self.longitude = longitude
            self.latitude = latitude

        def to_dict(self) -> dict:
            return {
                "Speed": self.speed,
                "Longitude": self.longitude,
                "Latitude": self.latitude
            }

    class Accelerometer:
        def __init__(self, acceleration_x: float, acceleration_y: float, acceleration_z: float,
                     gravity_x: float, gravity_y: float, gravity_z: float):
            self.acceleration_x = acceleration_x
            self.acceleration_y = acceleration_y
            self.acceleration_z = acceleration_z

            self.gravity_x = gravity_x
            self.gravity_y = gravity_y
            self.gravity_z = gravity_z

        @property
        def total_acceleration(self):
            return math.sqrt(self.acceleration_x ** 2 +
                             self.acceleration_y ** 2 +
                             self.acceleration_z ** 2)

        def to_dict(self) -> dict:
            return {
                "AccelerationX": self.acceleration_x,
                "AccelerationY": self.acceleration_y,
                "AccelerationZ": self.acceleration_z,

                "GravityX": self.gravity_x,
                "GravityY": self.gravity_y,
                "GravityZ": self.gravity_z,
            }

    class Gyroscope:
        def __init__(self, rotation_delta_matrix: list,
                     angle_speed_x: float, angle_speed_y: float, angle_speed_z: float):
            self.rotation_delta_matrix = rotation_delta_matrix
            self.angle_speed_x = angle_speed_x
            self.angle_speed_y = angle_speed_y
            self.angle_speed_z = angle_speed_z

        @property
        def total_angle_speed(self):
            return math.sqrt(self.angle_speed_x ** 2 +
                             self.angle_speed_y ** 2 +
                             self.angle_speed_z ** 2)

        def to_dict(self) -> dict:
            return {
                "RotationDeltaMatrix": self.rotation_delta_matrix,
                "AngleSpeedX": self.angle_speed_x,
                "AngleSpeedY": self.angle_speed_y,
                "AngleSpeedZ": self.angle_speed_z,
            }

    def __init__(self, frame_id: int, session_id: int, previous_frame_id: int,
                 time, gps: GPS, accelerometer: Accelerometer, gyroscope: Gyroscope):
        self.frame_id = frame_id
        self.session_id = session_id
        self.previous_frame_id = previous_frame_id
        self.time = time
        self.gps = gps
        self.accelerometer = accelerometer
        self.gyroscope = gyroscope

    def to_dict(self) -> dict:
        return {
            "FrameID": self.frame_id,
            "SessionID": self.session_id,
            "PreviousFrameID": self.previous_frame_id,
            "Time": self.time,
            "GPS": self.gps.to_dict(),
            "Accelerometer": self.accelerometer.to_dict(),
            "Gyroscope": self.gyroscope.to_dict(),
        }
