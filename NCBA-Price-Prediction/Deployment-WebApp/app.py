from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__,template_folder = 'templates')

# Load your saved model
model = joblib.load('ncba_prediction')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # Extracting input features
    opening_price = float(data['opening_price'])
    highest_price = float(data['highest_price'])
    lowest_price = float(data['lowest_price'])

    # Make prediction
    prediction = model.predict([[opening_price, highest_price, lowest_price]])

    # Return prediction
    return jsonify({'closing_price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
