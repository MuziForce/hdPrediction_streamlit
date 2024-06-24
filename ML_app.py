import pandas as pd 
import pickle
import sklearn
import streamlit as st 

pickle_in = open('finall_model.pkl', 'rb')
classifer = pickle.load(pickle_in)

print(sklearn.__version__)

def welcome():
    return "Welcome patient"

def prediction(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):

    prediction = classifer.predict(
        [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    )

    print(prediction)
    return prediction 

def main():

    st.title("Heart disease prediction")

    age = st.text_input("age", "Type Here")
    sex = st.text_input("sex", "Type Here")
    cp = st.text_input("chest pain", "Type Here")
    trestbps = st.text_input("trestbps", "Type Here")
    chol = st.text_input("chol", "Type Here")
    fbs = st.text_input("fbs", "Type Here")
    restecg = st.text_input("restecg", "Type Here")
    thalach = st.text_input("thalach", "Type Here")
    exang = st.text_input("exang", "Type Here")
    oldpeak = st.text_input("oldpeak", "Type Here")
    slope = st.text_input("slope", "Type Here")
    ca = st.text_input("ca", "Type Here")
    thal = st.text_input("thal", "Type Here")

    result = " "

    if st.button ("Predict"):
        result = prediction(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    st.success('The output is{}'.format(result))

if __name__ =='__main__':

    main()