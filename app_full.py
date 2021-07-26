from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from utils import AppUtils

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def query_records():
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


@app.route('/', methods=['POST'])
def create_record():
    # Get details from request
    name = request.args.get('name')
    email = request.args.get('email')

    # Create new user from data
    user = {'name': name, 'email': email}
    # Insert user into database
    insert = mongo.db.users.insert_one(user)

    # Acknowledge if insert was successful and return result
    if insert.acknowledged:
        return {'result': 'success'}
    else:
        return {'result': 'error'}


@app.route('/', methods=['DELETE'])
def delete_record():
    # Get details from request
    name = request.args.get('name')
    email = request.args.get('email')

    # Create user to be deleted form data
    user = {'name': name, 'email': email}

    # Delete user from database
    delete = mongo.db.users.delete_one(user)

    # Acknowledge and return result
    if delete.acknowledged:
        return {'result': 'success'}
    else:
        return {'result': 'error'}


@app.route('/update_by_name', methods=['PUT'])
def update_record_by_name():
    name = request.args.get('name')
    email = request.args.get('email')
    user = {'name': name, 'email': email}
    update = mongo.db.users.update_one({"name": user["name"]}, {"$set": user})
    if update.acknowledged:
        return {'result': 'success'}
    else:
        return {'result': 'error'}


if __name__ == "__main__":
    app.run(debug=True)
