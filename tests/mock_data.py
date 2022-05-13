import json

entry_test = {
    'start': '2018-06-12T13:48:14Z',
    'billable': 'true',
    'description': 'Writing documentation',
    'projectId': '5b1667790cb8797321f3d664',
    'taskId': '5b1e6b160cb8793dd93ec120',
    'end': '2018-06-12T13:50:14Z',
    'tagIds': ['5a7c5d2db079870147fra234'],
}
entry_test_json = json.loads(
    '{ "start": "2018-06-12T13:48:14Z", "billable": true, "description": "Writing documentation", "projectId": "5b1667790cb8797321f3d664", "taskId": "5b1e6b160cb8793dd93ec120", "end": "2018-06-12T13:50:14Z", "tagIds": ["5a7c5d2db079870147fra234"] }'
)
