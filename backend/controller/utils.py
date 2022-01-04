from flask import jsonify


def generate_response(status, message):
    response = jsonify({
        "status": status,
        "message": message
    })
    response.status_code = status
    return response