import requests
import json

from models import Frame, FrameBatch, Session
from parsers import frame_json_to_model, session_json_to_model

import pandas as pd


def load_frames_by_url(url: str) -> tuple[dict[list[Frame]], dict[Session]]:
    response = requests.get(url)
    data = json.loads(response.text)

    frames_by_session_id = dict()
    for frame_data in data.get("Frames"):
        frame = frame_json_to_model(frame_data)
        frames_by_session_id[frame.session_id] = frames_by_session_id.get(frame.session_id, list()) + [frame]

    sessions_by_session_id = dict()
    for session_data in data.get("Sessions"):
        session = session_json_to_model(session_data)
        sessions_by_session_id[session.session_id] = session

    return frames_by_session_id, sessions_by_session_id


def unite_frames_to_frame_batches(frames: list[Frame], session: Session, batch_size: int) -> list[FrameBatch]:
    batches = list()
    for i in range(0, len(frames), batch_size):
        batches.append(FrameBatch(frames[i:i+batch_size], session))
    return batches


def frame_batches_to_dataframe(batches: list[FrameBatch]):
    frame_batches_dict = dict()
    for batch in batches:
        for attribute, value in batch.__dict__.items():
            frame_batches_dict[attribute] = frame_batches_dict.get(attribute, list()) + [value]
    return pd.DataFrame(frame_batches_dict)
