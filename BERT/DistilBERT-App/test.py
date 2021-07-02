import ktrain
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1" # use only CPU in prediction

predictor = ktrain.load_predictor('distilbert')


def get_prediction(x):
	print('Received inside predict: ', x)
	sent = predictor.predict([x])
	print(sent)
	return sent[0]
x = 'this movie is great'

print(get_prediction(x))