# Resume-Classification-app
# Resume Classification using NLP & Streamlit Deployment

This project classifies resumes into specific job categories using NLP techniques and machine learning models. The app is deployed using **Streamlit Cloud** and hosted via **GitHub**.

---

##  Dataset

Resumes in `.docx` format were provided in a ZIP file. Each resume belongs to one of the following categories:

- React Developer
- SQL Developer
- Peoplesoft Resume
- Workday Resume

---

##  Project Workflow

### 1. Data Extraction
- Extracted `.docx` files from ZIP
- Converted to structured CSV format with `Resume` and `Category` columns

### 2. Exploratory Data Analysis (EDA)
- Class distribution plot
- Word count statistics
- Vocabulary insights

### 3. Preprocessing
- Cleaned text: lowercased, removed special characters
- TF-IDF vectorization (`max_features=3000`)
- Label encoding for target categories

### 4. Model Building
Trained 8 ML models:
- Logistic Regression (best )
- Naive Bayes
- SVC
- Decision Tree
- Random Forest
- Gradient Boosting
- Bagging
- Voting Classifier

### 5. Evaluation

- Evaluated all 8 models on accuracy, precision, recall, and F1-score.
- **Best Performing Model**: `Logistic Regression`  
  - **Accuracy**: 100.00%
  - Selected for final deployment.

### 6. Deployment
- App built using `Streamlit`
- Models saved using `joblib`
- Code & app deployed on GitHub + Streamlit Cloud

---

##  How to Use

🔗 **Live App**: https://resume-classification-app-sz7m5qtc3cwdeqxngbsqb5.streamlit.app

Paste your resume text into the app to get an instant category prediction.

---

## Files in This Repository

| File | Description |
|------|-------------|
| `app.py` | Streamlit frontend app |
| `resume_classifier.pkl` | Trained ML model |
| `tfidf_vectorizer.pkl` | TF-IDF vectorizer |
| `label_encoder.pkl` | Label encoder |
| `requirements.txt` | Python dependencies |
| `Resume_Classification_Project.ipynb` | Colab notebook with full ML pipeline |


---

## Sample Prediction Outputs

#### Sample Predictions from Final Model (Logistic Regression)

>  **Input Sample 1:**  
> *"Experienced Peoplesoft DBA with over 7 years of experience in PeopleTools, App Engine, and SQR development. Hands-on experience with FSCM modules."*  
>  **Predicted Category:** `Peoplesoft Resume`

---

>  **Input Sample 2:**  
> *"Developed responsive front-end applications using React.js and Redux. Experience with REST APIs and Git workflows in Agile environments."*  
>  **Predicted Category:** `React Developer`

---

>  **Input Sample 3:**  
> *"Strong SQL programming background with expertise in stored procedures, triggers, and query optimization. Worked extensively with Oracle and MySQL."*  
>  **Predicted Category:** `SQL Developer`

---

>  **Input Sample 4:**  
> *"Workday consultant with deep knowledge of HCM, Core HR, and integrations. Experience in Workday Studio and report writing."*  
>  **Predicted Category:** `Workday`


