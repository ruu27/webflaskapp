Ng Ru Ying AI300 Project

---
Deployed Flask AWS website: 
http://ec2-13-215-202-61.ap-southeast-1.compute.amazonaws.com/

Chosen model:
CatBoostClassifier

Model parameters:
 {'subsample': 0.8, 'loss_function': 'Logloss', 'learning_rate': 0.05, 'l2_leaf_reg': 1, 'iterations': 200, 'depth': 4, 'colsample_bylevel': 0.8}

Offline AUC:
0.90524

---
Key milestones: 
- SQL ETL from remote database
- Machine Learning and Model export to pkl file (catboost)
- Flask web app with HTML & CSS form input & model deployment
- AWS and Docker cloud deployment
- API prediction call from AWS website (api_request.ipynb)

----
Project Brief
Target: To determine how likely a customer will churn in the next month
Dataset: Telcom customer demographics & profiles, churn status

---
Steps
ETL
0. Data Extraction (SQL) - Data retrieval from remote database
1. Data Cleaning (Pandas) -  Filling missing values, changing dtypes
2. Data Exploration (Plotly) - Graphical visualization
3. Data Transformation (Pandas) - Choosing columns, Label Encoding relevant columns

MACHINE LEARNING
4. Experiment with various models
5. Evaluate accuracy (AUC, accuracy)
6. Choose best model (Catboost) and export to pkl file (model/model.pkl)
7. Use SHAP to determine most relevant features
(research_ohe.ipynb - initial iteration to consider feature importance
research.ipynb - final iteration with chosen features)

FLASK
- CSS & HTML formatting
- Main webpage (Python) - app.py

DOCKER
- Dockerfile for deploying onto Docker

AWS
- Deployment onto AWS (website above)
- API request call for predictions tested on Jupyter (api_request.ipynb)
Note: Predictions from CatBoostClassifier are only 0 or 1. Results have been converted to
"No, customer will not churn" or "Yes, customer will churn".
