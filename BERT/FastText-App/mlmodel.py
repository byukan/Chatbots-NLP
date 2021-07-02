from flask import Flask, request, jsonify
import fasttext_model as model


app = Flask(__name__)


@app.route('/')
def hello():
	return 'Congrats! Server is working'

# get the json data
@app.route('/get_prediction', methods = ['POST'])
def get_prediction():
	tx = request.get_json(force = True)
	text = tx['comment']

	pred = model.get_prediction(text)

	d = dict(pred)
	for key in d:
	    d[key] = str(d[key])

	return jsonify(result = d)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000, debug = True, use_reloader = False)	
