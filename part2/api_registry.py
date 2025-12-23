from flask import Flask
from flask_restx import Api
from presentation.api.users import api as users_ns
from presentation.api.amenities import api as amenities_ns
from presentation.api.places import api as places_ns
from presentation.api.reviews import api as reviews_ns

def create_app():
    app = Flask(__name__)
    api = Api(app, version="1.0", title="HBnB API")

    api.add_namespace(users_ns, path="/api/v1/users")
    api.add_namespace(amenities_ns, path="/api/v1/amenities")
    api.add_namespace(places_ns, path="/api/v1/places")
    api.add_namespace(reviews_ns, path="/api/v1/reviews")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
