import requests
import json

from models import Frame, FrameBatch
from parsers import frame_json_to_model

import pandas as pd


def load_frames_by_url(url: str) -> dict[list[Frame]]:
    response = requests.get(url)
    data = json.loads(response.text)
    frames_in_session = dict()
    for frame_data in data.get("Frames"):
        frame = frame_json_to_model(frame_data)
        frames_in_session[frame.session_id] = frames_in_session.get(frame.session_id, list()) + [frame]
    return frames_in_session


def unite_frames_to_frame_batches(frames: list[Frame], batch_size: int) -> list[FrameBatch]:
    batches = list()
    for i in range(0, len(frames), batch_size):
        batches.append(FrameBatch(frames[i:i+batch_size]))
    return batches


def frame_batches_to_dataframe(batches: list[FrameBatch]):
    frame_batches_dict = dict()
    for batch in batches:
        for attribute, value in batch.__dict__.items():
            frame_batches_dict[attribute] = frame_batches_dict.get(attribute, list()) + [value]
    return pd.DataFrame(frame_batches_dict)
