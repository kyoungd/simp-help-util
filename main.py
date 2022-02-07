import os
import json
from flask import Flask, render_template, request
from run_model import bag_of_words

apiservice = Flask(__name__)

@apiservice.route("/ping", methods=["GET"])
def home_view():
    return "pong"

@apiservice.route("/bag_of_words", methods=["POST"])
def help_view():
    message = request.json
    q = message['question']
    result = bag_of_words(q)
    return { 'status': 'OK', 'data': json.dumps(result) }

if __name__ == "__main__":
    apiservice.run()
