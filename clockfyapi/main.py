import json
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional

import atexit
import sys
import httpx
import argparse
from loguru import logger

from clockfyapi.config import settings

BASE_URL = 'https://api.clockify.me/api/v1'
HEADERS = {'content-type': 'application/json', 'X-Api-Key': settings.API_KEY}


def time_now() -> datetime:
    return datetime.now()


def list_clients():
    with httpx.Client() as client:
        return client.get(
            f'{BASE_URL}/workspaces/settings.WORKSPACE_ID/clients',
            headers=HEADERS,
        )


def list_client(client_id=settings.CLIENT_ID):
    with httpx.Client() as client:
        _URL = f'{BASE_URL}/workspaces/{settings.WORKSPACE_ID}/clients/{client_id}'
        logger.debug(_URL)
        return client.get(_URL, headers=HEADERS)


def list_projects():
    with httpx.Client() as client:
        _URL = f'{BASE_URL}/workspaces/{settings.WORKSPACE_ID}/projects'
        return client.get(_URL, headers=HEADERS)


def list_tasks_by_project_id(project_id=settings.PROJECT_ID):
    with httpx.Client() as client:
        _URL = f'{BASE_URL}/workspaces/{settings.WORKSPACE_ID}/projects/{project_id}/tasks'
        return client.get(_URL, headers=HEADERS)


def get_user():
    with httpx.Client() as client:
        # _URL = f'{BASE_URL}/user'
        _URL = f'{BASE_URL}/workspaces/{settings.WORKSPACE_ID}/users'
        user = client.get(_URL, headers=HEADERS)
        logger.info(user.json())


def start_work(start_date):
    with httpx.Client() as client:
        _start_date = start_date + timedelta(hours=3)
        _URL = f'{BASE_URL}/workspaces/{settings.WORKSPACE_ID}/time-entries'
        _data = TimeEntry(
            start=_start_date,
            description='Working tasks',
            projectId=settings.PROJECT_ID,
        )
        output = client.post(_URL, data=_data.to_json(), headers=HEADERS)
        logger.debug(_data.to_json())
        logger.debug(_start_date)
        logger.info(output)


def stop_work(stop_date):
    _stop_date = stop_date + timedelta(hours=3)
    def convert_datetime_to_str(date: datetime = time_now()):
        return date.strftime('%Y-%m-%dT%XZ')

    with httpx.Client() as client:
        date = convert_datetime_to_str(_stop_date)
        _URL = f'{BASE_URL}/workspaces/{settings.WORKSPACE_ID}/user/{settings.USER_ID}/time-entries'
        _data = dict(
            end=date,
        )
        logger.debug(_URL)
        logger.debug(date)
        logger.debug(_data)
        output = client.patch(_URL, json=_data, headers=HEADERS)
        logger.info(output)
        logger.info(output.url)
        logger.info(output.content)
        logger.info(output.json)


@dataclass
class TimeEntry:
    """Represent time entry"""

    start: datetime
    description: str
    projectId: str
    billable: Optional[bool] = field(repr=False, default=None)
    taskId: Optional[str] = field(repr=False, default=None)
    end: Optional[datetime] = field(repr=False, default=None)
    tagIds: Optional[List[str]] = field(repr=False, default_factory=list)

    def _convert_datetime_to_string(self, date: datetime = time_now()):
        return date.strftime('%Y-%m-%dT%XZ')

    def __post_init__(self):
        self.start = self._convert_datetime_to_string(self.start)
        self.end = (
            self._convert_datetime_to_string(self.end) if self.end else None
        )

    def __repr__(self) -> dict:
        return repr(self.__dict__)

    def to_json(self):
        return json.dumps(self.__dict__)


def main(*args):
    parser = argparse.ArgumentParser(description='Clockfy API CLI')
    parser.add_argument('method', choices=['start', 'stop', 'user'],
                        help='Start or Stop clockfy work time')
    parser.add_argument('-d', action='store_const', const=datetime.now(),
                        help='Datetime clockfy work time')
    args = parser.parse_args()
    match(args.method):
        case('start') if args.d:
            start_work(args.d)
        case('stop') if args.d:
            stop_work(args.d)
        case('user'):
            get_user()
        case _:
            raise Exception('Not found')


if __name__ == "__main__":
    main()
