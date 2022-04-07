from flask import Flask, jsonify

app = Flask(__name__)

items = [
    {
        'name': 'Muruga',
        'places': 'Vadapalani'
    },
    {
        'name': 'Tirupati',
        'places': 'Andhra'
    }
]


@app.route('/')
def index():
    # return {'message': 'Product Team..'}
    return jsonify(message='Product Team...')


@app.route('/items')
def fetch_items():
    return jsonify(items=items)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
