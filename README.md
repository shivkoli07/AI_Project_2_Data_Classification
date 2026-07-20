# AI Project - Iris Flower Classification

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-orange?logo=scikitlearn)
![Status](https://img.shields.io/badge/Project-Completed-success)

A Machine Learning classification project developed as part of the **DecodeLabs Artificial Intelligence Internship (Project 2)**.

---

# 📌 Project Overview

The **Iris Flower Classification** project is a supervised Machine Learning application that classifies Iris flowers into one of three different species based on their physical measurements.

The model learns patterns from historical flower data and predicts the species of a new flower using the **K-Nearest Neighbors (KNN)** classification algorithm.

The three flower species are:

- 🌸 Setosa
- 🌸 Versicolor
- 🌸 Virginica

---

# 🎯 Objective

The objective of this project is to understand the complete Machine Learning workflow, including:

- Loading datasets
- Data preprocessing
- Feature scaling
- Splitting data into training and testing sets
- Training a Machine Learning model
- Evaluating model performance
- Predicting new data

This project serves as an introductory implementation of supervised Machine Learning classification.

---

# ❓ What Does This Project Do?

This application allows users to:

- Load the Iris dataset
- Clean and preprocess the data
- Train a KNN classification model
- Test the model on unseen data
- Calculate prediction accuracy
- Generate a confusion matrix
- Predict the species of a new flower based on user input

---

# 💡 Why Is This Project Useful?

This project demonstrates how Machine Learning can automate classification tasks.

Instead of manually identifying flower species, the trained model predicts the correct species based on measurements with high accuracy.

The same workflow can later be applied to real-world problems such as:

- Disease prediction
- Email spam detection
- Customer segmentation
- Product recommendation
- Image classification
- Document classification
- Fraud detection

---

# 🚀 Features

- 📂 Load Iris Dataset
- 🧹 Data Cleaning & Preprocessing
- 📊 Feature Scaling
- 🔀 Train-Test Split
- 🤖 K-Nearest Neighbors (KNN) Model
- 📈 Model Evaluation
- 📉 Confusion Matrix Generation
- 📋 Accuracy & F1 Score Report
- 🌸 Predict New Flower Species

---

# 🛠 Technologies & Libraries Used

| Library | Purpose |
|----------|---------|
| **Python** | Main programming language used to develop the project. |
| **Pandas** | Loads and manages the dataset using DataFrames for easy data manipulation. |
| **NumPy** | Performs numerical computations and handles arrays efficiently. |
| **Matplotlib** | Creates visualizations such as the Confusion Matrix. |
| **Scikit-learn** | Provides Machine Learning algorithms, preprocessing tools, train-test split, evaluation metrics, and the KNN classifier. |
| **Joblib** | Saves and loads the trained Machine Learning model for future use. |

---

# 📂 Project Structure

```text
Data_Classification/
│
├── dataset/
│   └── iris.csv
│
├── models/
│   └── knn_model.pkl
│
├── outputs/
│   ├── accuracy_report.txt
│   ├── confusion_matrix.png
│   └── prediction_results.csv
│
├── src/
│   ├── load_data.py
│   ├── preprocess.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── predict.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/shivkoli07/AI_Project_2_Data_Classification.git
```

Move into the project folder

```bash
cd Data_Classification
```

Install all required libraries

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

# 📊 Machine Learning Workflow

```text
Load Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Scaling
      │
      ▼
Train-Test Split
      │
      ▼
Train KNN Model
      │
      ▼
Evaluate Model
      │
      ▼
Generate Accuracy Report
      │
      ▼
Predict New Flower Species
```

---

# 📈 Model Information

**Algorithm Used**

- K-Nearest Neighbors (KNN)

**Dataset**

- Iris Flower Dataset

**Training Split**

- 80%

**Testing Split**

- 20%

**Evaluation Metrics**

- Accuracy Score
- F1 Score
- Confusion Matrix

---

# 📁 Output Files

After running the project, the following files are automatically generated:

| File | Description |
|------|-------------|
| accuracy_report.txt | Stores model accuracy and F1 Score |
| confusion_matrix.png | Visual representation of prediction performance |
| knn_model.pkl | Saved trained Machine Learning model |

---

# 🔮 Future Improvements

Some possible enhancements include:

- Support for multiple ML algorithms
- Interactive GUI using Tkinter or Streamlit
- Web application using Flask or FastAPI
- Upload custom datasets
- Compare different classification models
- Hyperparameter tuning
- Cross-validation

---

# 👨‍💻 Author

**Shiv Koli**

Information Technology Student

DecodeLabs Artificial Intelligence Internship

GitHub: https://github.com/shivkoli07
