# 🛡️ Intelligent Anti-Money Laundering Detection System Using Artificial Neural Networks

## 📌 Project Overview

Money laundering is a major financial crime in which illegal money is transferred through financial transactions to make it appear legitimate. Traditional rule-based systems often struggle to identify complex and unusual transaction patterns.

This project develops an **Intelligent Anti-Money Laundering (AML) Detection System using Artificial Neural Networks (ANN)** to identify potentially suspicious financial transactions.

The trained ANN model analyzes transaction details and classifies transactions into two categories: Money Laundering and Not Money Laundering. A simple interactive web application is developed using Streamlit to make predictions based on user-provided transaction information.

## 🎯 Business Objective

The primary objective is to develop an intelligent machine learning solution that can:

- Identify potentially suspicious financial transactions.
- Distinguish between legitimate and money-laundering transactions.
- Support financial institutions in monitoring transaction activities.
- Reduce dependency on traditional rule-based detection methods.
- Provide a simple interface for transaction analysis.

## 📊 Features Used

The model uses the following six input features:

| Feature | Description |
|---|---|
| Amount | Transaction amount |
| Payment_currency | Currency used for making the payment |
| Received_currency | Currency received by the beneficiary |
| Sender_bank_location | Location of the sender's bank |
| Receiver_bank_location | Location of the receiver's bank |
| Payment_type | Type of financial transaction |

## 🤖 Machine Learning Approach

**Artificial Neural Network (ANN)** is used to learn patterns from transaction data and classify financial transactions.

The project involves the following workflow:

1. Data Loading and Understanding
2. Exploratory Data Analysis (EDA)
3. Data Cleaning and Preprocessing
4. Feature Transformation
5. Artificial Neural Network Model Development
6. Model Training and Evaluation
7. Model Saving and Serialization
8. Streamlit Application Development

## ⚙️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Deep Learning | TensorFlow, Keras |
| Preprocessing | Scikit-learn |
| Model Deployment | Streamlit |
| Model Serialization | Keras, Joblib |

## 🔍 Prediction Output

The trained ANN model produces two classification outputs:

| Class | Prediction |
|---|---|
| 0 | Not Money Laundering |
| 1 | Money Laundering |

The Streamlit application displays the final prediction based on the transaction details entered by the user.

## 🖥️ Streamlit Application

The application provides a simple interface where users can enter:

- Transaction Amount
- Payment Currency
- Received Currency
- Sender Bank Location
- Receiver Bank Location
- Payment Type

After entering the details, users can click the **Analyze Transaction** button to receive the prediction.

## 📁 Project Structure

```text
Intelligent-AML-Detection/
│
├── app.py
├── AIML.keras
├── preprocessor
├── requirements.txt
├── README.md
│
└── notebooks/
    └── model_development.ipynb
```

*The notebooks folder is optional.*

## 🚀 Installation and Execution

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd Intelligent-AML-Detection
```

### Step 3: Create a Virtual Environment

```bash
python -m venv myvenv
```

### Step 4: Activate the Environment

For Windows:

```bash
myvenv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Run the Streamlit Application

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

## 💡 Key Benefits

- Uses Artificial Neural Networks to learn transaction patterns.
- Supports binary classification of financial transactions.
- Accepts multiple transaction-related features.
- Provides an interactive and user-friendly interface.
- Demonstrates an end-to-end deep learning deployment workflow.

## ⚠️ Limitations

- Model predictions depend on the quality and representativeness of training data.
- Unseen categorical values may require additional preprocessing support.
- The system should be validated using real-world financial transaction data before operational use.
- Predictions are indicators for further investigation, not proof of criminal activity.

## 🔮 Future Enhancements

- Integrate real-time transaction monitoring.
- Implement anomaly detection techniques.
- Develop explainable AI techniques for prediction interpretation.
- Add transaction risk scoring.
- Deploy the application on a cloud platform.
- Integrate the system with financial transaction databases.

## 👨‍💻 Project Information

**Project Title:** Intelligent Anti-Money Laundering Detection System Using Artificial Neural Networks

**Domain:** Artificial Intelligence and Machine Learning

**Model:** Artificial Neural Network (ANN)

**Deployment:** Streamlit

---

⭐ If you find this project interesting, consider giving the repository a star!

**Disclaimer:** This project is developed for educational and research purposes. It is not a certified financial crime detection or compliance system.
