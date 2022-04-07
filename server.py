from flask import Flask, jsonify

app = Flask(__name__)

items = [
    {
        'name': 'Muruga',
        'place': 'Chennai'
    },
    {
        'name': 'Tirupati',
        'place': 'Andhra'
    }
]


@app.route('/')
def index():
    # return {'message': 'Working fine..'}
    return jsonify(message='Working fine...')


@app.route('/items')
def fetch_items():
    return jsonify(items=items)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
