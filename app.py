from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

items = []

class Items(Resource):
    def get(self):
        return {"items": items}

class Item(Resource):
    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item
        return {"Message": "Item not found."}, 404

    def post(self, name):
        data = request.get_json() #silent=True doesnt give an error and returns none, force=True doesnt care if header is not specified as json.
        new_item = {"name": name,
                    "price": data["price"]}
        items.append(new_item)
        return new_item, 201

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')


app.run(port=5000, debug=True)
