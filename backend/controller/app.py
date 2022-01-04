import os

from flask import Flask, jsonify

from controller.exceptions import BadRequestException


app = Flask(__name__)


@app.errorhandler(BadRequestException)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response


@app.route('/search', methods=['GET'])
def search():
    pass


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
