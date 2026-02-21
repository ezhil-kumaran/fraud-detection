# 💳 Fraud Detection System Using Scikit learn (Machine Learning)

A machine learning-based fraud detection system that identifies fraudulent financial transactions using advanced classification algorithms. The project includes comprehensive data analysis, model comparison, and an interactive web application for real-time fraud detection.

## DATASET USED

https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download

## 📋 Project Overview

This project analyzes financial transaction data to predict fraudulent activities using machine learning techniques. It compares multiple classification algorithms and provides actionable insights through feature importance analysis and model evaluation metrics.

## ✨ Features

- **Exploratory Data Analysis (EDA)**: Comprehensive analysis of transaction patterns and fraud indicators
- **Feature Engineering**: Created balance difference features to improve model performance
- **Multiple ML Models**: Implementation and comparison of Logistic Regression and Random Forest
- **Model Optimization**: Hyperparameter tuning for optimal performance
- **Feature Importance Analysis**: Identifies the most critical factors in fraud detection
- **Interactive Web App**: Streamlit-based application for real-time fraud prediction
- **Model Persistence**: Saves trained models for deployment

## 🛠️ Technologies Used

### Programming Language

- **Python 3.x**

### Data Analysis & Visualization

- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical data visualization

### Machine Learning

- **Scikit-learn** - Machine learning algorithms and tools
  - Logistic Regression
  - Random Forest Classifier
  - StandardScaler
  - OneHotEncoder
  - ColumnTransformer
  - Pipeline

### Model Deployment

- **Streamlit** - Interactive web application
- **Joblib** - Model serialization

### Development Environment

- **Jupyter Notebook** - Interactive development and analysis

## 📊 Dataset

The project uses a financial transaction dataset(https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset?resource=download) (`AIML Dataset.csv`) containing:

- Transaction types (CASH_IN, CASH_OUT, DEBIT, PAYMENT, TRANSFER)
- Transaction amounts
- Account balances (sender and receiver)
- Fraud labels

## 🔍 Methodology

### 1. Data Preprocessing

- Handled missing values
- Removed irrelevant features (nameOrig, nameDest, isFlaggedFraud, step)
- Created engineered features (balance differences)
- Applied StandardScaler for numerical features
- Used OneHotEncoder for categorical features

### 2. Model Development

- **Logistic Regression**: Baseline model with class balancing
- **Random Forest**: Advanced ensemble method with 100 estimators

### 3. Model Evaluation

- Classification reports (Precision, Recall, F1-Score)
- Confusion matrices
- Accuracy scores
- Feature importance analysis

### 4. Handling Imbalanced Data

- Used `class_weight='balanced'` parameter
- Stratified train-test split to maintain class distribution

## 📈 Key Insights

- **Feature Engineering**: Balance difference features significantly improved model performance
- **Transaction Types**: TRANSFER and CASH_OUT transactions are most susceptible to fraud
- **Model Comparison**: Random Forest outperformed Logistic Regression in fraud detection
- **Critical Features**: Balance changes and transaction amounts are key fraud indicators

## 🌐 Web Application

The Streamlit app provides an intuitive interface for fraud detection:

- Input transaction details
- Automatic balance difference calculation
- Real-time fraud prediction
- Probability scores for decision confidence

### Using the App

1. Enter transaction details (type, amount, balances)
2. Click "Check Transaction"
3. View prediction result and fraud probability

<img width="1032" height="931" alt="Screenshot 2026-02-21 232214" src="https://github.com/user-attachments/assets/a44e0375-2bbc-4ccf-a987-de935a6f2cc8" />
<img width="1108" height="959" alt="Screenshot 2026-02-21 232353" src="https://github.com/user-attachments/assets/3a9cd3cf-6615-464b-bf69-82c1951db72c" />


## 📊 Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | ~94%     |
| Random Forest       | ~95%     |



