import os

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

from infrastructure.repositories import MongoGarmentItemsRepository
from controller.exceptions import BadRequestException
from infrastructure.database import connect_to_database


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class Injector:
    MONGO_REPOSITORY = MongoGarmentItemsRepository()

    def get_repository(self):
        return self.MONGO_REPOSITORY


garment_items_repository = Injector().get_repository()
garment_items_repository.set_db_connection(connect_to_database())


@app.errorhandler(BadRequestException)
def handle_bad_request(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response


@app.route('/search', methods=['GET'])
@cross_origin()
def search():
    garment_items = garment_items_repository.find(request.args.get('q'))
    result = []
    for item in garment_items:
        result.append({
            "thumbnail": item.image_urls[0],
            "product_title": item.product_title,
            "stock": item.stock,
            "price": item.price,
            "currency": item.currency_code
        })
    return jsonify(result)


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
