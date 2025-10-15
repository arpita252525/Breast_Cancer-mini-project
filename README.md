# Breast_Cancer-mini-project

# 🩺 Breast Cancer Classification

## 📘 Project Overview
This project uses the **Breast Cancer Dataset** (from [Kaggle by Yasser H](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)) to classify tumors as **Malignant (M)** or **Benign (B)** based on cell nuclei features.  
The notebook performs **Exploratory Data Analysis (EDA)** and applies **machine learning models** to predict cancer type.

---

## 📂 Dataset Information
- **Source:** Kaggle – *yasserh/breast-cancer-dataset*  
- **Samples:** 569  
- **Features:** 30 numeric + 1 target (`diagnosis`)  
- **Target Values:**  
  - `M` → Malignant  
  - `B` → Benign  

Each feature represents computed measurements from breast cell images, such as:
- `radius_mean`, `texture_mean`, `perimeter_mean`, `area_mean`, `smoothness_mean`, etc.

---

## 🔍 Exploratory Data Analysis (EDA)
The EDA notebook (`BreastCancer.ipynb`) includes:
1. **Diagnosis Distribution** – Benign vs Malignant counts  
2. **Feature Comparison** – Average feature values per diagnosis  
3. **Correlation Heatmap** – Identifying strongly correlated features  
4. **Boxplots & Visualizations** – Understanding key variable impacts  
5. **Feature Importance** – Top predictors for malignancy

---

## 🤖 Model Building
Several classification models were trained and compared:
- Logistic Regression  
- Random Forest  
- Support Vector Machine (SVM)  
- Decision Tree  
- K-Nearest Neighbors (KNN)

The best-performing model achieved **over 95% accuracy** on the test data.

---

## ⚙️ Requirements
Install dependencies with:
```bash
pip install -r requirements.txt

