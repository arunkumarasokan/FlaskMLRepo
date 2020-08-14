
from flask import Flask, request, jsonify, render_template, url_for
import pickle


app = Flask(__name__)
pickle_in = open("ExxonOil.pickle", "rb")
linear = pickle.load(pickle_in)

@app.route('/')
def home():
    return 'Hello World'
    #return render_template('home.html')
    #return render_template('index.html')


@app.route('/predict/<oilprice>', methods=['POST', 'GET'])
def predict(oilprice):
    if request.method == 'GET':
        op = float(oilprice)
        prediction = linear.predict([[op]])
        predicted_value = prediction[0][0]
        return {"oil_price": oilprice, "EXXON Price": predicted_value}

if __name__ == '__main__':
    app.run(debug=True)