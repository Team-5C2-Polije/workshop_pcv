from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/test', methods=['GET'])
def test():
    # Mengambil parameter 'name' dari query string
    name = request.args.get('name')

    if name:
        response = {
            "message": f"Hello, {name}!"
        }
    else:
        response = {
            "error": "No name provided"
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
