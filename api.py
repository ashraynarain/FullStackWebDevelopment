from flask import Flask, jsonify, request

app = Flask(__name__)

users = []
transactions = []

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    for user in users:
        if user['username'] == username:
            return jsonify(user)
    return jsonify({'error': 'User not found'}), 404


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    balance = data.get('balance')
    new_user = {
        'username': username,
        'password': password,
        'email': email,
        'balance': balance
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users', methods=['DELETE'])
def delete_all_users():
    global users
    users = []
    return jsonify({'message': 'All users deleted'})

@app.route('/users/<username>', methods=['DELETE'])
def delete_user(username):
    for user in users:
        if user['username'] == username:
            users.remove(user)
            return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'User not found'}), 404

@app.route('/users/<username>', methods=['PUT'])
def update_user(username):
    for user in users:
        if user['username'] == username:
            data = request.get_json()
            user['password'] = data.get('password', user['password'])
            user['email'] = data.get('email', user['email'])
            user['balance'] = data.get('balance', user['balance'])
            return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/transactions', methods=['GET'])
def get_transactions():
    return jsonify(transactions)

@app.route('/transactions/<transaction_id>', methods=['GET'])
def get_transaction(transaction_id):
    for transaction in transactions:
        if transaction['transaction_id'] == transaction_id:
            return jsonify(transaction)
    return jsonify({'error': 'Transaction not found'}), 404


@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    from_username = data.get('from_username')
    to_username = data.get('to_username')
    amount = data.get('amount')

    from_user = None
    to_user = None

    for user in users:
        if user['username'] == from_username:
            from_user = user
        elif user['username'] == to_username:
            to_user = user

    if from_user is None or to_user is None:
        return jsonify({'error': 'Invalid users in transaction'}), 400

    if amount <= 0:
        return jsonify({'error': 'Amount must be greater than zero'}), 400

    if from_user['balance'] < amount:
        return jsonify({'error': 'Insufficient balance for the transaction'}), 400

    transaction_id = len(transactions) + 1
    new_transaction = {
        'from_username': from_username,
        'to_username': to_username,
        'transaction_id': transaction_id,
        'amount': amount
    }
    transactions.append(new_transaction)

    from_user['balance'] -= amount
    to_user['balance'] += amount

    return jsonify(new_transaction), 201


if __name__ == '__main__':
    app.run(debug=True)
