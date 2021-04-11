from typing import Union, List


def make_response(status: int, data: Union[dict, List[dict]]) -> dict:
    response = {
        'status': status,
        'data': data,
    }
    return response
