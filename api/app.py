import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/test', methods=['GET'])
def test():
    response = {
        'message': "New block forgeif nod",
        'index': "index",
        'transaction': "block'transactions'",
        'proof': "proof",
        'previous_hash': "block['previous_hash']"
    }
    return jsonify(response), 200


# @app.route('/transactions/new', methods=['POST'])
# def new_transaction():
#     values = request.get_json()

#     required = ['sender', 'recipient', 'amount']
#     if not all(k in values for k in required):
#         return "Missing values", 400
#     index = blockchain.new_transaction(
#         values['sender'], values['recipient'], values['amount']
#     )
#     response = {
#         'message' : f'Transaction will be added to Block {index}'
#     }
#     return jsonify(response), 201

# @app.route('/fullchain', methods=['GET'])
# def full_chain():
#     response = {
#         'chain': blockchain.chain,
#         'length': len(blockchain.chain)
#     }
#     return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
