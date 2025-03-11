'''
Processes inputs for model

original model input:
{'contract_type': 2.0,
 'internet_type': 0.0,
 'payment_method': 1.0,
'num_referrals': 9.0,
 'num_dependents': 2.0,
 'tenure_months': 71.0,
 'total_monthly_fee': 19.8,
 'paperless_billing': 0.0,
 'age': 52.0}

0 sample (raw website input):
{'contract_type': 2.0,
 'internet_type': 0.0,
 'payment_method': 1.0, 
 'num_referrals': 9.0,
 'num_dependents': 2.0,
 'tenure_months': 71.0,
 'total_monthly_fee': 19.8,
  'paperless_billing': 0.0,
 'age': 52.0}

 1 sample (raw website input):
 {'contract_type': 0.0,
 'internet_type': 1.0,
 'payment_method': 0.0,
 'num_referrals': 0.0,
 'num_dependents': 0.0,
 'tenure_months': 51.0,
 'total_monthly_fee': 97.8,
  'paperless_billing': 1.0,
 'age': 70.0}

'''
import numpy as np

def format_model_inputs(input_dict):
    '''
    Fixes order of input to match model input order. Converts to int/float.
    '''
    # Version 1: Fixes order of input to match model
    result_dict = {'contract_type': None,
 'internet_type': None,
 'payment_method': None,
 'num_referrals': None,
 'num_dependents': None,
 'tenure_months': None,
 'total_monthly_fee': None,
 'paperless_billing': None,
 'age': None}
    # All results should be an int. only total_monthly_fee is float
    for key, value in input_dict.items():
        if key != 'total_monthly_fee':
            try:
                result_dict[key] = int(value)
            except:
                print(f'Error converting {key} to int')
        else:
            try:
                result_dict[key] = float(value)
            except:
                print(f'Error converting {key} to float')

    result = list(result_dict.values())
    return result
    # Version 2: Assumes form input follows model input order
    # result_list = []
    # for k, v in input_dict.items():
    #     try:
    #         if k != 'total_monthly_fee':
    #             result_list.append(int(input_dict[k]))
    #         else:
    #             result_list.append(float(input_dict[k]))
    #     except:
    #         print(f'{k} error')
    # return result_list



def validate(input_dict):
    '''
    Checks if all fields are input, if fields are converted to int/float correctly
    '''
    errors = []
    required_fields = ['contract_type', 'internet_type',
            'payment_method', 'num_referrals',
            'num_dependents', 'tenure_months',
            'total_monthly_fee', 'paperless_billing',
            'age']
    for field in required_fields:
        print(field)

        if field not in input_dict:
            errors.append(f'{field} not found in request.')

        if field in ['age', 'num_referrals', 'num_dependents','tenure_months'] and type(input_dict[field]) != int \
                and not input_dict[field].isnumeric():
            errors.append(f'{field}: Age, num_referrals, num_dependents and tenure_months fields must be int type.')

        elif field == 'total_monthly_fee' and type(input_dict[field]) != float:
            try:
                float(input_dict['total_monthly_fee'])
            except ValueError:
                errors.append(f'Total Monthly Fee field must be numeric.')

    return errors