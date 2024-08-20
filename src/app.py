from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello World!'

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        todos.pop(position)
        return jsonify(todos)
    except IndexError:
        return jsonify({"error": "Todo not found"}), 404

@app.route('/todos/bulk', methods=['POST'])
def add_multiple_todos():
    request_body = request.json
    if isinstance(request_body, list):
        todos.extend(request_body)
        return jsonify(todos)
    else:
        return jsonify({"error": "Invalid input. Expected a list of todos."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)