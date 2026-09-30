# 🏭 Industrial Pump Maintenance Prediction

A **machine learning-based predictive maintenance application** that estimates whether an industrial pump requires maintenance using sensor and operational measurements.

The project implements an end-to-end machine learning workflow covering **data exploration, preprocessing, feature analysis, classification, model evaluation, error analysis, and deployment using Streamlit**.

🔗 **Live Application:**  
https://industrial-machine-failure-prediction-pmsvbmeue5ifk6qrcuahtc.streamlit.app/

---

## 🎯 Project Objective

Industrial equipment continuously generates operational data such as temperature, vibration, pressure, flow rate, rotational speed, and operating hours.

The objective of this project is to investigate whether these measurements can be used to identify pumps that require maintenance.

The project focuses on:

- 🔍 Understanding industrial sensor data
- 📊 Performing exploratory data analysis
- 🧹 Preparing data for machine learning
- 🤖 Comparing classification models
- 📈 Evaluating predictive performance
- 🔎 Performing model error analysis
- 💾 Saving the trained model
- 🌐 Deploying the prediction system using Streamlit

> **Note:** The available dataset provides a `Maintenance_Flag` rather than a directly documented "failure within a defined operating window" label. Therefore, `Maintenance_Flag` is used as the prediction target in this educational implementation.

---

## 📌 Problem Statement

Predict whether an industrial pump requires maintenance based on its sensor and operational measurements.

The system takes measurements such as **temperature, vibration, pressure, flow rate, RPM, and operational hours** and predicts whether the pump is classified as requiring maintenance.

The project is based on **Problem 21: Industrial Machine Failure Prediction** from the Learn Depth Academy LLP Track 1 Final Capstone.

---

## 🗂️ Dataset

The project uses the **Large Industrial Pump Maintenance Dataset** available through Kaggle.


**Dataset Source:** `selonamaris/large-industrial-pump-maintenance-dataset`

### Dataset Characteristics

| Property | Value |
|---|---:|
| Observations | 20,000 |
| Columns | 8 |
| Industrial Pumps | 5 |
| Target | `Maintenance_Flag` |

### Features

| Feature | Description |
|---|---|
| `Pump_ID` | Identifier of the industrial pump |
| `Temperature` | Pump temperature |
| `Vibration` | Pump vibration measurement |
| `Pressure` | Pump pressure |
| `Flow_Rate` | Pump flow rate |
| `RPM` | Rotational speed |
| `Operational_Hours` | Total operating hours |
| `Maintenance_Flag` | Binary maintenance target |

---
---


## 🎯 Target Variable

The prediction target is:
```text
Maintenance_Flag
```
| Value         | Meaning                         |
| ------------- | ------------------------------- |
| `0`           | No maintenance required         |
| `1`           |       Maintenance required      |

---
## 🧬 Features Used for Prediction
The following six variables are used as model inputs:
```text
Temperature
Vibration
Pressure
Flow_Rate
RPM
Operational_Hours
```
`Pump_ID`  is excluded because it acts as an identifier rather than a direct sensor or operational measurement.

The target variable is also excluded from the input features to prevent target leakage.

---
---
## Machine Learning Workflow

The project follows a complete machine learning pipeline:
```text
Industrial Pump Dataset
          │
          ▼
   Data Quality Analysis
          │
          ▼
 Exploratory Data Analysis
          │
          ▼
    Feature Selection
          │
          ▼
    Train / Test Split
          │
          ▼
 Classification Models
          │
     ┌────┼────┐
     ▼    ▼    ▼
 Logistic  Decision  KNN
Regression  Tree
     │    │    │
     └────┼────┘
          ▼
   Model Evaluation
          │
          ▼
    Error Analysis
          │
          ▼
     Final Model
          │
          ▼
   Saved Model (.pkl)
          │
          ▼
     Streamlit App
          │
          ▼
 Maintenance Prediction
```

## 📊 Exploratory Data Analysis

Several analyses were performed to understand the dataset before modelling.

**Data Quality**

The analysis included:
- Dataset dimensions
- Data types
- Missing-value analysis
- Duplicate detection
- Descriptive statistics
- Descriptive statistics

**Feature Analysis**

The project also investigated:
- Feature distributions
- Boxplots
- Feature correlations
- Mutual information
- Pump-level maintenance distributions
- IQR-based outlier detection
- Potential data leakage

**Key Findings**

The exploratory analysis showed:

- The dataset contains 20,000 observations.
- No missing values were identified.
- No duplicate rows were identified.
- The two maintenance classes were approximately balanced.
- No IQR-based outliers were detected in the six predictive features.
- The feature distributions showed substantial overlap between maintenance classes.
- Individual feature correlations with the target were very small.
- Mutual-information scores were also very small.

These findings suggested that the available features may contain limited information for distinguishing the two maintenance classes.

---

---

### 🤖 Machine Learning Models

Three foundational classification algorithms were evaluated:

**1. Logistic Regression**

Used as a linear classification baseline.

**2. Decision Tree**

Used to model potentially nonlinear relationships between sensor measurements and maintenance status.

The final Decision Tree configuration was:
```text
DecisionTreeClassifier(
    max_depth=20,
    random_state=42
)
```
**3. K-Nearest Neighbours (KNN)**
Used as a distance-based classification baseline.
Decision Tree and KNN configurations were evaluated using 5-fold cross-validation on the training data.

---


---

### 📈 Model Evaluation

The final Decision Tree was evaluated on a held-out test set.

| METRIC        | RESULT                          |
| ------------- | ------------------------------- |
| Accuracy      | 49.98%                          |
| Precision     | 49.84%                          |
| Recall        | 55.42%                          |
| F1-Score      | 52.48%                          |
|ROC-AUC        | 0.513                           |


### Confusion Matrix

|              | Predicted 0 | Predicted 1 |
| ------------ | ----------: | ----------: |
| **Actual 0** |         894 |       1,112 |
| **Actual 1** |         889 |       1,105 |

---

### 🔎 Model Interpretation

The model achieved approximately 50% accuracy, while the ROC-AUC was approximately 0.5.

This indicates that the available sensor and operational variables provide limited predictive discrimination for the `Maintenance_Flag`  target in this dataset.

Therefore, the trained model should be considered an **educational machine learning prototype**, rather than a production-ready predictive maintenance system.

This result is also an important finding of the project: a machine learning model does not necessarily become useful simply because a dataset contains multiple sensor measurements.

------
## 🧪 Error Analysis

The final model generated:
- 1,112 False Positives
- 889 False Negatives

Both error types occurred frequently, indicating substantial overlap between the two target classes.

Some differences were observed between false-positive and false-negative observations, particularly for:
- `RPM` 
- `Operational_Hours` 

However, these differences were not sufficient to produce strong overall class discrimination.
This analysis highlights the importance of examining where a model fails, rather than relying only on a single performance metric.

-----
## 🌐 Streamlit Application

A lightweight Streamlit interface was developed to demonstrate the trained model.

User Inputs
The application accepts:
- 🌡️ Temperature
- 📳 Vibration
- 🧭 Pressure
- 💧 Flow Rate
- ⚙️ RPM
- ⏱️ Operational Hours

**Output**
The application provides:
-Predicted maintenance class
-Estimated probability of maintenance
The application loads the saved Decision Tree model and uses the same feature structure used during model training.

**🚀 Live Demo**
Try the application here:
https://industrial-machine-failure-prediction-pmsvbmeue5ifk6qrcuahtc.streamlit.app/

-----
---

## 🏗️ Project Architecture

```text
                    ┌──────────────────┐
                    │   Pump Sensors   │
                    └────────┬─────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │    Dataset / CSV       │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │   Data Preprocessing   │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │         EDA            │
                │ Correlation • MI •     │
                │ Distributions • Outliers│
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │   Feature Selection    │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │ Classification Models  │
                │                        │
                │ Logistic Regression    │
                │ Decision Tree          │
                │ KNN                    │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │    Model Evaluation    │
                │ Accuracy • F1 • AUC    │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │     Trained Model      │
                │  decision_tree.pkl     │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │     Streamlit App      │
                └────────────┬───────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │ Maintenance Prediction │
                └────────────────────────┘
```
---

---

## 📁 Project Structure

```text
Industrial_Machine_Failure_Prediction/
│
├── 00_Full_Experiment.ipynb
├── requirements.txt
├── download_data.py
│
├── app/
│   └── app.py
│
├── data/
│
├── figures/
│
├── models/
│   ├── decision_tree_model.pkl
│   └── feature_names.pkl
│
└── notebooks/
    ├── 01_EDA.ipynb
    ├── 02_Model_Development.ipynb
    └── 03_Model_Evaluation.ipynb
```
---
## 🛠️ Technologies Used

- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📊 Matplotlib
- 📈 Seaborn
- 🤖 Scikit-learn
- 💾 Joblib
- 🌐 Streamlit
- 📓 Jupyter Notebook

-----
---
##  ⚙️ Installation
 Clone the repository
```text
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Industrial_Machine_Failure_Prediction
```
 Create a virtual environment
Creating a virtual environment is recommended.
```text
python -m venv myenv
```
Windows PowerShell
```text
myenv\Scripts\Activate.ps1
```
macOS / Linux
```text
source myenv/bin/activate
```
 Install the required dependencies:
```text
pip install -r requirements.txt
```
 Running the application
Start the Streamlit application:
```text
streamlit run app.py
```
The application will open in your browser at:
```text
http://localhost:8501
```
📓 Reproducing the Experiment
The complete experiment can be reproduced using:
```text
00_Full_Experiment.ipynb
```
The complete experiment can be reproduced using:
```text
01_EDA.ipynb
02_Model_Development.ipynb
03_Model_Evaluation.ipynb
```
---
---
## ⚠️ Limitations

This project has several important limitations.

**Dataset Limitations**

Information such as:
- Historical failure events
- Maintenance history
- Component-level degradation
- Time-series sensor patterns
- Environmental conditions
- Failure timestamps
is not available in the current dataset.

## Target Limitation
The dataset provides a Maintenance_Flag, but it does not directly document a time-to-failure or failure-within-operating-window target.

Therefore, this project should not be interpreted as a validated **Remaining Useful Life (RUL)** or failure forecasting system.

## Model Performance
The final model achieved an ROC-AUC of approximately **0.513**, indicating limited predictive signal in the available variables.

Consequently, the model is intended for **educational demonstration and machine learning workflow development**, not real-world maintenance decision-making.

-----
## 🔮 Future Improvements

Several extensions could make the system more useful for predictive maintenance research:

- Incorporate time-series sensor measurements
- Add historical maintenance records
- Include actual failure timestamps
- Engineer rolling-window sensor features
- Investigate temporal patterns in vibration and temperature
- Evaluate Random Forest and Gradient Boosting models
- Explore XGBoost or LightGBM
- Apply probability calibration
- Investigate explainable AI techniques such as SHAP
- Evaluate models using time-based validation
- Develop anomaly-detection approaches
- Use richer industrial datasets containing actual failure events



-----
## 🎓 Learning Outcomes
This project demonstrates practical experience with an end-to-end machine learning workflow:
```text
Problem Definition
        ↓
Data Understanding
        ↓
EDA
        ↓
Feature Selection
        ↓
Model Development
        ↓
Cross-Validation
        ↓
Model Evaluation
        ↓
Error Analysis
        ↓
Model Serialization
        ↓
Streamlit Deployment
```
The project also demonstrates an important machine learning principle:
****A model's performance must be interpreted in the context of the information contained in the dataset.****
A low-performing model can still provide useful insight when its limitations are properly investigated and communicated.

-----
## 👩‍💻 Author
Sreekutty Santhosh
