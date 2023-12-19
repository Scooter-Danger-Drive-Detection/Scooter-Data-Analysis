from models.ride_mode import RideMode


class Session:
    def __init__(self, session_id: int, user_id: int, ride_mode: RideMode, session_db_id=-1):
        self.session_id = session_id
        self.user_id = user_id
        self.ride_mode = ride_mode
        self.session_db_id = session_db_id

    def to_dict(self) -> dict:
        return {
            "SessionID": self.session_id,
            "UserID": self.user_id,
            "RideMode": self.ride_mode.key
        }
