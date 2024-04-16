import pickle
import streamlit as st
import pandas as pd

# Page config
st.set_page_config(
    page_title="Bank Loan Classification",
    page_icon="images/image.jpg",
    layout="wide",
)

# Page title
st.title('Bank Loan - Loan Prediction')
st.image('images/image.jpg')
st.write("\n\n")

st.markdown(
    """
    This app aims to assist in predicting bank loan between being Charged Off and Fully Paid
    , thereby reducing the time required to analyze machine problems.
    """
)

# Load the model
with open('model/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit interface to input data
col1, col2, col3 = st.columns(3)

with col1:
    current_loan_amount = st.number_input(label='Current Loan Amount')
    term = st.selectbox(label='Term Type', options=["Short Term", "Long Term"])
    credit_score = st.number_input(label='Credit Score')
    annual_income = st.number_input(label='Annual Income')
    years_in_current_job = st.selectbox(label='Years in current job', options=["0-1 year", "2-3 years", "4-6 years",
                                                                               "7-9 years", "+10 years"])

with col2:
    home_ownership = st.selectbox(label='Home Ownership', options=["Rent", "Home Mortgage", "Own Home"])
    purpose = st.selectbox(label='Loan Purpose', options=["Personal", "Debt Consolidation", "Business Loan", "Other"])
    monthly_debt = st.number_input(label='Monthly Debt')
    years_of_credit_history = st.number_input(label='Years of Credit History')
    no_of_open_accounts = st.number_input(label='Number of open accounts')

with col3:
    no_of_credit_problems = st.selectbox(label='Number of credit problems', options=["0", "1", "2", "3", "4", "5", "6",
                                                                                     "7"])
    current_credit_balance = st.number_input(label='Current Credit Balance')
    max_open_credit = st.number_input(label='Maximum open credit')
    bankruptcies = st.selectbox(label='Bankruptcies', options=["0", "1", "2", "3", "4", "5"])
    tax_liens = st.selectbox(label='Tax Liens', options=["0", "1", "2", "3", "4", "5", "6"])


# Function to predict the input
def prediction(current_loan_amount, term, credit_score, annual_income, years_in_current_job,
               home_ownership, purpose, monthly_debt, years_of_credit_history, no_of_open_accounts,
               no_of_credit_problems, current_credit_balance, max_open_credit, bankruptcies, tax_liens):

    if term == "Short Term":
        term = 1
    else:
        term = 0

    if years_in_current_job == "0-1 year":
        years_in_current_job = 0
    elif years_in_current_job == "2-3 years":
        years_in_current_job = 2
    elif years_in_current_job == "4-6 years":
        years_in_current_job = 3
    elif years_in_current_job == "7-9 years":
        years_in_current_job = 4
    else:
        years_in_current_job = 1

    if home_ownership == "Home Mortgage":
        home_ownership = 0
    elif home_ownership == "Own Home":
        home_ownership = 1
    else:
        home_ownership = 2

    if purpose == "Business Loan":
        purpose = 0
    elif purpose == "Debt Consolidation":
        purpose = 1
    elif purpose == "Other":
        purpose = 2
    else:
        purpose = 3

    # Create a df with input data
    df_input = pd.DataFrame({
        'Current Loan Amount': [current_loan_amount],
        'Term': [term],
        'Credit Score': [credit_score],
        'Annual Income': [annual_income],
        'Years in current job': [years_in_current_job],
        'Home Ownership': [home_ownership],
        'Purpose': [purpose],
        "Monthly Debt": [monthly_debt],
        'Years of Credit History': [years_of_credit_history],
        'Number of Open Accounts': [no_of_open_accounts],
        'Number of Credit Problems': [no_of_credit_problems],
        'Current Credit Balance': [current_credit_balance],
        'Maximum Open Credit': [max_open_credit],
        'Bankruptcies': [bankruptcies],
        'Tax Liens': [tax_liens],
    })

    prediction = model.predict(df_input)

    if prediction[0] == 0:
        prediction = "Charged Off"
    else:
        prediction = "Fully Paid"
    return prediction


# Botton to predict
if st.button('Predict'):
    predict = prediction(current_loan_amount, term, credit_score, annual_income, years_in_current_job,
                         home_ownership, purpose, monthly_debt, years_of_credit_history, no_of_open_accounts,
                         no_of_credit_problems, current_credit_balance, max_open_credit, bankruptcies,
                         tax_liens)
    st.write("Your Bank Loan is {}".format(predict))
    st.success(predict)
