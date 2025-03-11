'''
Main website app file
'''
from flask import Flask, request, render_template
from input_processing import validate #, format_model_inputs, format_prediction
from model import predict_and_format #Model

app = Flask(__name__)

# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Input from website form
        form_input = dict(request.form)
        print(form_input)
        # Check if fields are input correctly
        errors = validate(form_input)
        if len(errors) > 0:
            return render_template('index.html', errors=errors)
        formatted_pred = predict_and_format(form_input)
        return render_template('index.html', formatted_pred=formatted_pred, form_input=form_input)
    return render_template('index.html')

# Method 2: Via POST API (one prediction at a time)
@app.route('/api/predict_one', methods=['POST'])
def predict_one():
    print(request.json)
    request_data = request.get_json()  # optional: print request_data as log
    print(request_data)
    errors = validate(request_data)
    if len(errors) > 0:
        return {'errors': errors}, 400
    formatted_pred = predict_and_format(request_data)
    return {'prediction': formatted_pred} # cannot have prediction: prediction because prediction is not in the html


# Method 2: Via POST API (many predictions at a time)
@app.route('/api/predict', methods=['POST'])
def predict_many():
    request_data = request.get_json()
    print(request_data)
    predictions = []
    for row in request_data:
        errors = validate(row)
        if len(errors) > 0:
            return {'record': row, 'errors': errors}, 400
        formatted_pred = predict_and_format(row)
        predictions.append(formatted_pred)
    return {'predictions': predictions}

if __name__ == '__main__':
    app.run(debug=True)