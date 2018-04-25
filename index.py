import DBService 
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/user', methods=['GET'])
def get_allusers():
    DBService.DBConnect("UserData.db", "User")
    DBService.checkTableReady()
    selectResult = DBService.select_All()
    DBService.DBClose()
    return jsonify({'users': selectResult})

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    DBService.DBConnect("UserData.db", "User")
    DBService.checkTableReady()
    try:
        selectResult = DBService.select_By_ID(user_id)
    except:
        abort(404)
        DBService.DBClose()
    
    DBService.DBClose()
    return jsonify({'users': selectResult})

@app.route('/api/user', methods=['POST'])
def add_user():
    if not request.json or not 'name' in request.json or not 'birthday' in request.json:
        abort(404)
        DBService.DBClose()

    DBService.DBConnect("UserData.db", "User")
    DBService.checkTableReady()
    
    try:
        id = DBService.insert(request.json['name'], request.json['birthday'])

        selectResult = DBService.select_By_ID(id)
    except:
        abort(404)
        DBService.DBClose()

    DBService.DBClose()
    return jsonify({'users': selectResult})

@app.route('/api/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    DBService.DBConnect("UserData.db", "User")
    DBService.checkTableReady()
    try:
        DBService.delete(user_id)
    except:
        abort(404)
        DBService.DBClose()
    
    DBService.DBClose()
    return jsonify({'result': True})

@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if not request.json or not 'name' in request.json or not 'birthday' in request.json:
        abort(404)

    DBService.DBConnect("UserData.db", "User")
    DBService.checkTableReady()
    try:
        DBService.update(user_id, request.json['name'], request.json['birthday'])
    except:
        abort(404)
        DBService.DBClose()
    
    DBService.DBClose()
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)