'''
Model load and predict
'''
import joblib
from input_processing import format_model_inputs

class Model:
    def __init__(self):
        try:
            PATH = 'model/model.pkl' # for docker run
            self.model = joblib.load(PATH)
        except:
            PATH = '../model/model.pkl' # for local run
            self.model = joblib.load(PATH)

    def predict(self, input_features):
        return self.model.predict(input_features)

def predict_and_format(form_input):
    '''
    Runs formatting of inputs to model, model predict, and formatting of 0 and 1 results to respective statements
    '''
    # Format inputs to correctly fit model (order, type)
    model_inputs = format_model_inputs(form_input)
    print('MODEL INPUTS', model_inputs)
    # Predict
    print(f'Model loaded : {Model()}')
    prediction = Model().predict(model_inputs)
    if prediction == 1:
        formatted_pred = 'Yes, customer will churn'
        print('Model predicted 1')
    elif prediction == 0:
        formatted_pred = 'No, customer will not churn'
        print('Model predicted 0')
    else:
        formatted_pred = 'Error in prediction (neither 0 or 1). Check with administrator.'
        print('Error in prediction (neither 0 or 1).')
    return formatted_pred

if __name__ == '__main__':
    model = Model()
    print(model)