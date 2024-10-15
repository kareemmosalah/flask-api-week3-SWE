from flask import jsonify, request
from app import app

# Endpoint 1: Welcome message
@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to the Flask API"}), 200

# Endpoint 2: Add two numbers
@app.route('/add', methods=['POST'])
def add():
    data = request.json
    if not data or 'num1' not in data or 'num2' not in data:
        return jsonify({"error": "Missing parameters"}), 400
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({"result": result}), 200

# Endpoint 3: Multiply two numbers
@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.json
    if not data or 'num1' not in data or 'num2' not in data:
        return jsonify({"error": "Missing parameters"}), 400
    num1 = data['num1']
    num2 = data['num2']
    result = num1 * num2
    return jsonify({"result": result}), 200

# Endpoint 4: Get item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    items = {1: "Book", 2: "Pen", 3: "Notebook"}
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"item": items[item_id]}), 200

# Endpoint 5: Delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    items = {1: "Book", 2: "Pen", 3: "Notebook"}
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    return jsonify({"message": f"Item {item_id} deleted"}), 200
