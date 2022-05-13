import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from src.config import settings
from loguru import logger

import httpx

BASE_URL= 'https://api.clockify.me/api/v1'
HEADERS = {'content-type': 'application/json', 'X-Api-Key': settings.API_KEY}
def time_now() -> datetime:
    return datetime.now()

def list_clients():
    with httpx.Client() as client:
        return client.get(f'{BASE_URL}/workspaces/settings.WORKSPACE_ID/clients', headers=HEADERS)

def list_client(client_id=settings.CLIENT_ID):
    with httpx.Client() as client:
        _URL =f'{BASE_URL}/workspaces/{settings.WORKSPACE_ID}/clients/{client_id}'
        logger.debug(_URL)
        return client.get(_URL, headers=HEADERS)

def list_projects():
    with httpx.Client() as client:
        _URL =f'{BASE_URL}/workspaces/{settings.WORKSPACE_ID}/projects'
        return client.get(_URL, headers=HEADERS)

def list_tasks_by_project_id(project_id=settings.PROJECT_ID):
    with httpx.Client() as client:
        _URL =f'{BASE_URL}/workspaces/{settings.WORKSPACE_ID}/projects/{project_id}/tasks'
        return client.get(_URL, headers=HEADERS)


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


