from flask import Flask, jsonify  # import flask
import json

app = Flask(__name__)  # create an app instance
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/first")  # at the end point /
def first():  # call method hello
    f = open('data/SE_first.json')
    json_data = json.load(f)
    return jsonify(json_data)  # which returns "hello world"


@app.route("/second")  # at the end point /
def second():  # call method hello
    f = open('data/SE_second.json')
    json_data = json.load(f)
    return jsonify(json_data)  # which returns "hello world"

@app.route("/third")  # at the end point /
def third():  # call method hello
    f = open('data/SE_third.json')
    json_data = json.load(f)
    return jsonify(json_data)  # which returns "hello world"


if __name__ == "__main__":  # on running python app.py
    app.run(host='0.0.0.0', port=3000)  # run the flask app
