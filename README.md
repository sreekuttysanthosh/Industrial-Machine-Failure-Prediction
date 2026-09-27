@"

\# Industrial Pump Maintenance Prediction



\## 1. Project Overview



This project develops an end-to-end machine learning prototype for predicting whether an industrial pump requires maintenance based on sensor and operational measurements.



The project is based on Problem 21: Industrial Machine Failure Prediction from the Learn Depth Academy LLP Track 1 Final Capstone.



The solution uses free and open-source Python tools and includes data exploration, preprocessing, foundational machine learning models, evaluation, error analysis, and a lightweight Streamlit application.



\## 2. Problem Statement



Predict whether a machine is likely to experience a failure within a defined operating window.



For this educational implementation, the available dataset provides a binary `Maintenance\_Flag` rather than a directly documented failure-within-operating-window label. Therefore, the project uses `Maintenance\_Flag` as the prediction target.



\## 3. Project Objective



Develop an end-to-end machine learning solution that:



\- Investigates the assigned dataset

\- Performs data quality analysis and EDA

\- Prepares the data

\- Builds foundational classification models

\- Evaluates model performance

\- Performs error analysis

\- Saves the final trained model

\- Demonstrates prediction through a Streamlit application



\## 4. Dataset



Dataset:



Large Industrial Pump Maintenance Dataset



Source:



Kaggle — `selonamaris/large-industrial-pump-maintenance-dataset`



Dataset characteristics:



\- 20,000 observations

\- 8 columns

\- 5 industrial pumps



\### Dataset Features



| Feature | Description |

|---|---|

| Pump\_ID | Pump identifier |

| Temperature | Pump temperature |

| Vibration | Pump vibration measurement |

| Pressure | Pump pressure |

| Flow\_Rate | Pump flow rate |

| RPM | Rotational speed |

| Operational\_Hours | Operating hours |

| Maintenance\_Flag | Binary maintenance target |



\## 5. Target Variable



`Maintenance\_Flag`



\- `0` = No maintenance required

\- `1` = Maintenance required



\## 6. Features Used for Prediction



The following six variables were used as predictive features:



\- Temperature

\- Vibration

\- Pressure

\- Flow\_Rate

\- RPM

\- Operational\_Hours



`Pump\_ID` was excluded because it is an identifier rather than a sensor or operational measurement.



The target variable `Maintenance\_Flag` was also excluded from the input features to prevent direct target leakage.



\## 7. Exploratory Data Analysis



The following investigations were performed:



\- Dataset shape and structure

\- Data types

\- Missing-value analysis

\- Duplicate detection

\- Descriptive statistics

\- Class balance

\- Feature distributions

\- Boxplots

\- Class-wise feature analysis

\- Correlation analysis

\- Mutual information

\- Pump-level target distribution

\- IQR-based outlier detection

\- Data leakage check



\### Main EDA Findings



\- Dataset contains 20,000 observations.

\- No missing values were identified.

\- No duplicate rows were identified.

\- The target classes were approximately balanced.

\- No IQR-based outliers were detected in the six predictive features.

\- Feature distributions showed substantial overlap between the two maintenance classes.

\- Correlations between individual features and the target were very small.

\- Mutual-information scores were also very small.



\## 8. Machine Learning Models



Three foundational classification approaches were evaluated:



1\. Logistic Regression

2\. Decision Tree

3\. K-Nearest Neighbours (KNN)



The Decision Tree and KNN hyperparameters were evaluated using 5-fold cross-validation on the training data.



\## 9. Final Model



The final prototype uses:



\*\*Decision Tree Classifier\*\*



Configuration:



\- `max\_depth = 20`

\- `random\_state = 42`



The final model was selected after comparing the evaluated foundational approaches.



\## 10. Model Evaluation



The final Decision Tree achieved the following results on the held-out test set:



| Metric | Result |

|---|---:|

| Accuracy | 49.98% |

| Precision | 49.84% |

| Recall | 55.42% |

| F1-score | 52.48% |

| ROC-AUC | 0.513 |



\### Confusion Matrix



| | Predicted 0 | Predicted 1 |

|---|---:|---:|

| Actual 0 | 894 | 1112 |

| Actual 1 | 889 | 1105 |



\### Interpretation



The model achieved approximately 50% accuracy and an ROC-AUC close to 0.5.



This indicates that the available sensor and operational variables provide limited predictive discrimination for the `Maintenance\_Flag` target in this dataset.



Therefore, the model is treated as an educational prototype rather than a reliable production maintenance predictor.



\## 11. Error Analysis



The final model produced:



\- 1,112 false positives

\- 889 false negatives



The substantial number of both error types indicates that the two target classes are difficult to distinguish using the available features.



Some differences were observed between false-positive and false-negative feature means, particularly for RPM and Operational\_Hours. However, these differences did not result in strong overall class discrimination.



\## 12. Streamlit Application



A lightweight Streamlit application was developed.



The application accepts:



\- Temperature

\- Vibration

\- Pressure

\- Flow Rate

\- RPM

\- Operational Hours



It then provides:



\- Predicted maintenance class

\- Estimated probability of maintenance



The application uses the saved Decision Tree model.



\## 13. Project Structure



```text

Industrial\_Machine\_Failure\_Prediction/

│

├── 00\_Full\_Experiment.ipynb

├── requirements.txt

├── download\_data.py

│

├── app/

│   └── app.py

│

├── data/

│

├── figures/

│

├── models/

│   ├── decision\_tree\_model.pkl

│   └── feature\_names.pkl

│

└── notebooks/

&#x20;   ├── 01\_EDA.ipynb

&#x20;   ├── 02\_Model\_Development.ipynb

&#x20;   └── 03\_Model\_Evaluation.ipynb

https://industrial-machine-failure-prediction-pmsvbmeue5ifk6qrcuahtc.streamlit.app/
