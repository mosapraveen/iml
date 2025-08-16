# 🎓 Student Performance Prediction

This project focuses on predicting student performance in entrance exams using machine learning techniques. By analyzing test scores and related features, the system assists in evaluating admission chances and academic outcomes.

---

## 📌 Project Overview
- Built a predictive model to analyze student performance.  
- Used **supervised learning algorithms** for classification and prediction tasks.  
- Dataset: [Admission_Predict.csv](https://www.kaggle.com/datasets/maicolab/university-admission) & custom datasets.  
- Features include:  
  - **Prueba 3 (Test 3 Score)**  
  - **Puntaje Final (Final Score)**  
  - **Puntaje Final Arquitectura (Final Architecture Score)**  
- Target Variable: **Observación** (performance category/department prediction).  

---

## 🚀 Key Features
- Data preprocessing and cleaning for better model accuracy.  
- Model training with **Logistic Regression, Decision Trees, and Random Forests**.  
- Performance evaluation using accuracy, precision, recall, and F1-score.  
- Flask-based web application for real-time predictions:  
  - Input: Test scores (0–100).  
  - Output: Predicted performance/department.  

---

## 🛠️ Tech Stack
- **Languages**: Python, HTML, CSS, Flask  
- **Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn  
- **Tools**: Jupyter Notebook, GitHub  

---

## 📊 Workflow
1. **Data Preprocessing** → Handle missing values, normalization, encoding.  
2. **Exploratory Data Analysis (EDA)** → Visualizations of score distributions & correlations.  
3. **Model Building** → Train/test split, apply ML algorithms.  
4. **Evaluation** → Compare models on multiple metrics.  
5. **Deployment** → Flask app for user interaction.  

---

## 💻 How to Run
1. Clone the repository:  
   ```bash
   git clone https://github.com/mosapraveen/iml.git
   cd iml
