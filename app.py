
import streamlit as st
import joblib

model = joblib.load('resume_classifier.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

def predict_resume_category(resume_text):
    cleaned = resume_text.lower()
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)
    label = label_encoder.inverse_transform(pred)[0]
    return label

st.title("Resume Category Classifier")
input_text = st.text_area("Paste your resume content here:")
if st.button("Predict"):
    if input_text.strip():
        result = predict_resume_category(input_text)
        st.success(f"Predicted Category: **{result}**")
    else:
        st.warning("Please paste some resume content.")
