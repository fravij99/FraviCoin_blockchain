from flask import Flask, jsonify, request
from blocklib import Blockchain
app = Flask(__name__)

# Creare oggetto Blockchain
blockchain = Blockchain()

# Route per minare un nuovo blocco
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        'message': 'A block is MINED',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }

    return jsonify(response), 200

# Route per visualizzare la blockchain
@app.route('/get_chain', methods=['GET'])
def display_chain():
    response = {'chain': blockchain.chain, 'length': len(blockchain.chain)}
    return jsonify(response), 200

# Route per verificare la validità della blockchain
@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)
    response = {'message': 'The Blockchain is valid.'} if valid else {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200

# Avviare il server Flask
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


# main.py

@app.route('/register_user', methods=['POST'])
def register_user():
    json_data = request.get_json()
    username = json_data.get('username')
    
    if not username:
        return 'Missing username', 400
    
    user_id = blockchain.register_user(username)
    response = {'message': 'User registered successfully', 'user_id': user_id}
    return jsonify(response), 201

# Route per effettuare una transazione
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    json_data = request.get_json()
    transaction_keys = ['sender_id', 'receiver_id', 'amount']
    
    if not all(key in json_data for key in transaction_keys):
        return 'Missing transaction information', 400

    sender_id = json_data['sender_id']
    receiver_id = json_data['receiver_id']
    amount = json_data['amount']

    index = blockchain.add_transaction(sender_id, receiver_id, amount)
    
    if index:
        response = {'message': f'This transaction will be added to Block {index}'}
        return jsonify(response), 201
    else:
        return 'Transaction failed: insufficient balance', 400

# Route per ottenere il saldo di un utente
@app.route('/get_balance/<user_id>', methods=['GET'])
def get_balance(user_id):
    balance = blockchain.get_user_balance(user_id)
    response = {'user_id': user_id, 'balance': balance}
    return jsonify(response), 200

@app.route('/list_good', methods=['POST'])
def list_good():
    json_data = request.get_json()
    user_id = json_data['user_id']
    good_name = json_data['good_name']

# Avvia il server
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
