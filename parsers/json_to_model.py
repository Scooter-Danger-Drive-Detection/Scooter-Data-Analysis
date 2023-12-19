from models import Frame, Session, get_ride_mode_by_key


def frame_json_to_model(data):
    gps_data = data.get("GPS")
    gps = Frame.GPS(gps_data.get("Speed"), gps_data.get("Longitude"), gps_data.get("Latitude"))

    accelerometer_data = data.get("Accelerometer")
    accelerometer = Frame.Accelerometer(accelerometer_data.get("AccelerationX"),
                                        accelerometer_data.get("AccelerationY"),
                                        accelerometer_data.get("AccelerationZ"),
                                        accelerometer_data.get("GravityX"),
                                        accelerometer_data.get("GravityY"),
                                        accelerometer_data.get("GravityZ"))

    gyroscope_data = data.get("Gyroscope")
    gyroscope = Frame.Gyroscope(gyroscope_data.get("RotationDeltaMatrix"),
                                gyroscope_data.get("AngleSpeedX"),
                                gyroscope_data.get("AngleSpeedY"),
                                gyroscope_data.get("AngleSpeedZ"))

    frame = Frame(data.get("FrameID"), data.get("SessionID"), data.get("PreviousFrameID"),
                  data.get("Time"), gps, accelerometer, gyroscope)
    return frame


def session_json_to_model(data):
    session = Session(data.get("SessionID"), data.get("UserID"),
                      get_ride_mode_by_key(data.get("RideMode")))
    return session
