"""
Flask App for LHS
"""

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from utils import AppUtils

# Create an instance of Flask for our app
app = Flask(__name__)

# Connect to our mongo database
app.config['MONGO_URI'] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def query_records():
    """
    Query records in database
    :return: JSON of the records returned
    """
    # Get details from request
    name = request.args.get('name')
    email = request.args.get('email')

    # Form search query
    query = AppUtils.make_search_query(email, name)

    # Search database
    users = mongo.db.users.find(query)

    # Get output into form we want
    output = [AppUtils.object_id_to_string(user) for user in users]

    # Return JSON of users
    return jsonify(output)


# This is the bit that runs:
if __name__ == "__main__":
    # Start the flask app
    app.run()
