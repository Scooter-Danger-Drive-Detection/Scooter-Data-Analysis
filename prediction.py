from model_loader import get_model
from models import Frame, Session
from transformations import unite_frames_to_frame_batches, frame_batches_to_dataframe


model_filename = "data_files/model.pickle"
parameters = ["average_acceleration", "min_acceleration", "max_acceleration", "average_angle_speed", "min_angle_speed", "max_angle_speed"]
target = "ride_mode"


def get_prediction(frames: list[Frame], session: Session, batch_size: int):
    model = get_model(model_filename)
    batches = unite_frames_to_frame_batches(frames, session, batch_size)
    df = frame_batches_to_dataframe(batches)
    predicts = model.predict(df[parameters])
    return sum(predicts) / len(predicts)
