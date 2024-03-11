from flask import jsonify


def get_response(status: int, body):
    """
    get_response creates the common response from the server
    """
    data = {
        "status": status,
        "body": body
    }

    return jsonify(data)
