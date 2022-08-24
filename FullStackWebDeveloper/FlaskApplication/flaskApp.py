from flask import Flask , jsonify , request

app = Flask(__name__)

stores = [

    {
        'name' :'My store',
        'items' :[
            {
                'name':'My item',
                'price' :13.99
            }
        ]
    }
]



"""post -> used to send data
    get -> used to send data back only
    
    here we are the server
"""

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'not found'})
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store[name] == name:
            new_item = {
                'name': request_data['name'],
                'item' :request_data['item']
            }

            store['items'].append(new_item)

            return jsonify(new_item)

    return jsonify({'error':'already available/store not found'})

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'error':'items not found'})








app.run(port=5000)