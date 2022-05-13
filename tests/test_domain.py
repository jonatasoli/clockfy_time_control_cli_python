from datetime import datetime

import pytest
import json

from src.main import TimeEntry
from tests.mock_data import entry_test, entry_test_json


def test_time_entry_required_only():
    time_entry = TimeEntry(
        start=datetime(2018, 6, 12, 13, 48, 14),
        description='Writing documentation',
        projectId='5b1667790cb8797321f3d664',
    )
    assert time_entry.start == entry_test['start']
    assert time_entry.description == entry_test['description']
    assert time_entry.projectId == entry_test['projectId']


def test_time_entry_in_dict_format():
    time_entry = TimeEntry(
        start=datetime(2018, 6, 12, 13, 48, 14),
        billable=True,
        description='Writing documentation',
        projectId='5b1667790cb8797321f3d664',
        taskId='5b1e6b160cb8793dd93ec120',
        end=datetime(2018, 6, 12, 13, 50, 14),
        tagIds=['5a7c5d2db079870147fra234'],
    )
    assert time_entry.start == entry_test['start']
    assert time_entry.end == entry_test['end']
    assert time_entry.billable == True
    assert time_entry.description == entry_test['description']
    assert time_entry.projectId == entry_test['projectId']
    assert time_entry.taskId == entry_test['taskId']


def test_time_entry_in_json_format():
    time_entry = TimeEntry(
        start=datetime(2018, 6, 12, 13, 48, 14),
        billable=True,
        description='Writing documentation',
        projectId='5b1667790cb8797321f3d664',
        taskId='5b1e6b160cb8793dd93ec120',
        end=datetime(2018, 6, 12, 13, 50, 14),
        tagIds=['5a7c5d2db079870147fra234'],
    )
    assert time_entry.__dict__ == entry_test_json

def test_list_projects_in_clockfy():
    ...



def test_time_start_in_api():
    ...


def test_time_start_when_already_time_started():
    ...


def test_time_stop_in_api():
    ...


def test_time_stop_in_api_when_time_already_stoped():
    ...


