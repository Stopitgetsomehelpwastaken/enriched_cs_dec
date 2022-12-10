from flask import Flask, render_template, request, jsonify
import time
import json
from random_word_gen import random_word_generator
my_server = Flask("mishra")


@my_server.route('/')
def input_html():
    return render_template('./input.html')

#Todo register route.
@my_server.route('/get_exercise', methods=['GET'])
def get_exercise():
	args = request.args
	print(args)
	print(args['num'])
	# time.sleep(0)
	# Call random word generator from here. 
	# Take the number of words from the request
	# return "hellp"
	words = random_word_generator(int(args['num']))
	d = {}
	d["words"] = words
	return json.dumps(d), 200



@my_server.route('/main')
def hello():
    return 'Hello, Shresth!'


if __name__ =="__main__":
	my_server.run(debug=True, host="127.0.0.1", port="5001")
