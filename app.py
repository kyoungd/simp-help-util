import os
import json
from flask import Flask, render_template, request
from run_model import bag_of_words

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def home_view():
    return "pong"

@app.route("/bag_of_words", methods=["POST"])
def help_view():
    message = request.json
    q = message['question']
    result = bag_of_words(q)
    return { 'status': 'OK', 'data': json.dumps(result) }

if __name__ == "__main__":
    env_port = os.environ.get('PORT', 5000)
    env_host = os.environ.get('HOST', '0.0.0.0')
    app.run(debug=False, host=env_host, port=env_port)
