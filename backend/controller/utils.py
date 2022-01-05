from flask import jsonify, Response


def generate_response(status: int, message: str) -> Response:
    """Generates a standard JSON response given a status code
    and a message.

    Args:
        status (int): Status of the response.
        message (str): Message related to the response.

    Returns:
        Response: Serialized response generated.

    """
    response = jsonify({
        "status": status,
        "message": message
    })
    response.status_code = status
    return response
