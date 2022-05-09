import httpx
from typing import List
from dataclasses import dataclass
from datetime import datetime



"""
{
  "start": "2018-06-12T13:48:14.000Z",
  "billable": "true",
  "description": "Writing documentation",
  "projectId": "5b1667790cb8797321f3d664",
  "taskId": "5b1e6b160cb8793dd93ec120",
  "end": "2018-06-12T13:50:14.000Z",
  "tagIds": [
    "5a7c5d2db079870147fra234"
  ],
  "customFields": [
    {
      "customFieldId" : "5b1e6b160cb8793dd93ec120",
      "value": "San Francisco"
    }
  ]
}
"""

@dataclass
class TimeEntry:
    """Represent time entry"""
    start: datetime
    billable: bool
    description: str
    projectId: str
    taskId: str
    end: datetime
    tagIds: List[str]

