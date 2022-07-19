from pathlib import Path
import pandas as pd
import os
import csv
import datetime

STATUS_HEADER = [
    "subject", "session", "type", "event", "timestamp", "source", "note"
]
DEFAULT_CACHE_PATH = "./.pipeline/status_log.csv"

def _load_records(cache_path: os.PathLike) -> pd.DataFrame:
    records: pd.DataFrame = pd.read_csv(cache_path)
    records = records.astype(
        {'date': 'datetime64', 'subject_id': 'string'}
    )
    return records


def _get_records_latest(records: pd.DataFrame) -> pd.DataFrame:
    latest_records = records.sort_values(
        'date', ascending=False
    ).groupby(
        ['subject_id', 'type'], dropna=False, as_index=False
    ).agg({
        'date': 'max',
        'event': 'first',
        'notes': 'first'}
    )
    return latest_records


def _get_records_by_type(records: pd.DataFrame, 
                        type="bids_conversion") -> pd.DataFrame:
    records_by_type = records.loc[
        records['type'] == type
    ]
    return records_by_type


def _get_records_by_event(records: pd.DataFrame,
                          type="submitted") -> pd.DataFrame:
    records_by_event = records.loc[
        records['event'] == "submitted"
    ]


def needs_processing(subjects: list, cache_path: os.PathLike, 
                     type="bids_conversion"):
    try:
        records = _load_records(cache_path)
    except FileNotFoundError:
        return subjects

    latest_records = _get_records_latest(records)
    latest_records_type = _get_records_by_type(latest_records, type=type)
    latest_records_event = _get_records_by_event(
        latest_records_type, type=type)

    completed = latest_records_event['subject_id'].tolist()

    needs_processing = [x for x in subjects if x not in completed]
    return needs_processing


def write_record(subject: str, session: str="", 
                 cache_path: os.PathLike=DEFAULT_CACHE_PATH,
                 type="bids_conversion", event="submitted",
                 note="clpipe generated"):
    timestamp = datetime.datetime.now()
    cache_path = Path(cache_path)

    if not cache_path.exists():
        cache_path.parent.mkdir(parents=True)
        with open(cache_path, "w") as cache_file:
            csv_writer = csv.writer(cache_file)
            csv_writer.writerow(STATUS_HEADER)

    with open(cache_path, "a") as cache_file:
        csv_writer = csv.writer(cache_file)
        csv_writer.writerow(
            [subject, session, type, event, timestamp, "", note]
        )
