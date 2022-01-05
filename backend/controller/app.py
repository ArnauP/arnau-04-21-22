from pymongo.errors import OperationFailure
from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request

from infrastructure.repositories import MongoGarmentItemsRepository
from infrastructure.database import connect_to_database
from controller.exceptions import BadRequestException
from controller.utils import generate_response

import os


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class Injector:
    """Contains the repositories related to the database type."""
    MONGO_REPOSITORY = MongoGarmentItemsRepository()

    def get_repository(self):
        return self.MONGO_REPOSITORY


garment_items_repository = Injector().get_repository()
garment_items_repository.set_db_connection(connect_to_database())


@app.errorhandler(BadRequestException)
def handle_bad_request(error):
    return generate_response(400, str(error))


@app.errorhandler(OperationFailure)
def handle_operation_failure(error):
    return generate_response(500, 'Database operation failed.')


@app.route('/')
def index():
    return generate_response(200, 'Alive')


@app.route('/search', methods=['GET'])
@cross_origin()
def search():
    query = request.args.get('q')
    if not query:
        raise BadRequestException(
            'Invalid query parameters key for the given values.')
    garment_items = garment_items_repository.find(query)
    result = [{
            "_id": str(item.id),
            "thumbnail": item.image_urls[0],
            "product_title": item.product_title,
            "stock": item.stock,
            "price": item.price,
            "currency": item.currency_code
        } for item in garment_items]
    return jsonify(result)


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
