# Bank Loan Status Prediction 

### To Access the Web App:
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_red.svg)](https://bank-loan-classification-prediction.streamlit.app)

## 1- Project Description:
Bank Loan Status via Classification Algorithms which helps in predicting if your bank loan is Fully Paid or Charged Off

## 2- Dataset :
- The dataset is two csv files one for train algorithms to find the best one and the other for testing them.
- Each file contains 19 columns & more than 10k rows
- Here is a link where you can get the data: **[Dataset Source](#https://www.kaggle.com/datasets/zaurbegiev/my-dataset)**

## 3- Notebook:
- My testing environment for different algorithms using different metrics and compare between them to find the best one before deployment
- Here is a link where you can find the notebook: **[Kaggle Notebook](#https://www.kaggle.com/code/ahmedashrafhelmi/bank-loan-classification-with-f1-score-0-911)**

## 4- Steps
- Get an overview about the data
- Clean data from missing and duplicates
- Data Visualization & EDA to get some insights
- Trying different Machine Learning Models like XGBoost, RandomForestClassifier ..,etc.
- Hyperparameter Tuning for top-3 models with the highest metric
- Testing model on test data
- Model Deployment using streamlit as web app

## 5- Project Structure

| Filename         | Description                                                                   |
|------------------|-------------------------------------------------------------------------------|
| Dataset          | contains two files; train_data & test_data                                    |
| Notebook         | contains the notebook of the project with visualization and all testing steps |
| images           | contains images used in the web app by streamlit                              |
| model            | contains model as pickle file after exporting                                 |
| streamlit_app    | contains the python file of the streamlit app                                 |
| requirements.txt | contains the requirements of libraries to run the notebook and app            |
| README.md        | An overview of the Repository and Project                                     |

