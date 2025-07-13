from .operator_request import OperatorRequest
from .request_registry import save_request

def submit_operator_command(operator_id, content, category="guidance"):
    request = OperatorRequest(operator_id, content, category)
    save_request(request.serialize())
    return request.id