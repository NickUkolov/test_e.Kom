from flask import Flask, request, jsonify
from utilities import validate_form

app = Flask(__name__)


@app.route('/get_form', methods=['POST'])
def find_form():

    result = validate_form(request.form)
    return jsonify(result)


if __name__ == '__main__':
    app.run()
