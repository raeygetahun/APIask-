from flask import Flask, request, jsonify
import datetime


app = Flask(__name__)

@app.route('/delivery_fee', methods=['POST'])
def delivery_fee():
    return jsonify({'delivery_fee':'hi'})
if __name__ == '__main__':
    app.run(debug=True)
