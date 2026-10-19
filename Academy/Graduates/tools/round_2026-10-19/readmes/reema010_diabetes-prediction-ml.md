# Diabetes Prediction with Machine Learning

An end-to-end binary classification project that predicts whether a patient has diabetes (`1`) or does not have diabetes (`0`). The project covers the complete machine learning workflow, from data exploration and preprocessing to model training, evaluation, and explainability using SHAP.

> **Training Program:** أساليب تعلم الآلة المتقدمة — *Applied Machine Learning for Intelligent Systems*  
> **Organization:** SDAIA Academy  
> **SDAIA Academy GitHub:** [github.com/SDAIAAcademy](https://github.com/SDAIAAcademy)

## Project Overview

This project applies supervised machine learning to a synthetic patient dataset and compares two gradient-boosting classification models:

- **XGBoost**
- **LightGBM**

The goal is not only to build a diabetes classifier, but also to demonstrate how raw data is explored, cleaned, transformed, evaluated, and interpreted in a complete applied machine learning workflow.

## Objectives

- Explore the dataset and understand the available features.
- Identify missing values, duplicates, invalid values, and inconsistent categorical data.
- Prepare the data for machine learning through cleaning, imputation, encoding, and standardization.
- Train XGBoost and LightGBM classifiers.
- Evaluate model performance using several classification metrics.
- Use SHAP to understand which features influence model predictions.

## Dataset

The notebook generates a **synthetic patient dataset** for educational purposes. It starts with 1,500 patient records and intentionally introduces common data-quality issues such as missing values, invalid zero values, inconsistent text labels, and duplicate rows.

The main features are:

| Feature | Description |
|---|---|
| `PatientID` | Unique patient identifier |
| `Age` | Patient age |
| `Gender` | Patient gender |
| `BMI` | Body Mass Index |
| `Glucose` | Glucose measurement |
| `BloodPressure` | Blood pressure measurement |
| `Insulin` | Insulin measurement |
| `FamilyHistory` | Family history of diabetes |
| `SmokingStatus` | Never, Former, or Current smoker |
| `ActivityLevel` | Low, Medium, or High physical activity |
| `Diabetes` | Target variable: `0` = no diabetes, `1` = diabetes |

## Project Workflow

The project follows these main steps:

1. Set up the environment and create the dataset.
2. Understand the dataset structure and features.
3. Perform exploratory data analysis on individual features and relationships between features.
4. Handle invalid values and missing data.
5. Remove duplicate records and clean inconsistent text values.
6. Convert categorical variables into numerical format.
7. Analyze correlations between features.
8. Split the data into training and testing sets.
9. Standardize selected numerical features.
10. Train XGBoost and LightGBM models.
11. Evaluate both models using classification metrics and curves.
12. Use SHAP to explain model predictions.

## Data Preprocessing

The preprocessing stage includes:

- Treating zero values in `Glucose` and `BloodPressure` as invalid values and replacing them with missing values.
- Filling missing numerical values in `BMI`, `Glucose`, `BloodPressure`, and `Insulin` using the median.
- Filling missing `SmokingStatus` values using the mode.
- Removing duplicate rows.
- Standardizing inconsistent gender labels such as `Male`, `male`, `M`, `Female`, `female`, and `F`.
- Removing `PatientID` before modeling because it is an identifier rather than a predictive feature.
- Mapping binary and ordinal categorical variables into numerical values.
- Applying one-hot encoding to `SmokingStatus`.

## Train/Test Split and Standardization

The data is divided into training and testing sets using:

- **Training data:** 80%
- **Testing data:** 20%
- **Random state:** 42
- **Stratification:** based on the diabetes target

The following numerical features are standardized using `StandardScaler`:

- `Age`
- `BMI`
- `Glucose`
- `BloodPressure`
- `Insulin`

The scaler is fitted only on the training data and then applied to both the training and testing sets to avoid data leakage.

## Models

### XGBoost

The XGBoost classifier is trained using the following main settings:

```python
XGBClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=4,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
)
```

### LightGBM

The LightGBM classifier is trained using:

```python
LGBMClassifier(
    n_estimators=300,
    learning_rate=0.05,
    num_leaves=15,
    min_child_samples=20,
    subsample=0.8,
    subsample_freq=1,
    colsample_bytree=0.8,
    random_state=42,
    verbose=-1,
)
```

## Model Evaluation

The models are evaluated using:

- Confusion Matrix
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- PR-AUC / Average Precision
- ROC Curve
- Precision-Recall Curve

The notebook also includes a manual exercise showing how TP, TN, FP, and FN are used to calculate classification metrics.

### Results

Results from the current notebook run:

| Metric | XGBoost | LightGBM |
|---|---:|---:|
| Accuracy | 0.793 | **0.803** |
| Precision | 0.646 | **0.677** |
| Recall | 0.519 | 0.519 |
| F1 Score | 0.575 | **0.587** |
| ROC-AUC | **0.823** | 0.821 |
| PR-AUC | 0.652 | **0.657** |

These results show the performance of the models on the synthetic dataset used in this project and should not be interpreted as clinical performance.

## Model Explainability with SHAP

SHAP is used with the XGBoost model to better understand how individual features influence its predictions.

The notebook includes:

- A **global feature importance plot** to show which features have the largest overall impact.
- A **beeswarm plot** to show the direction and magnitude of feature effects across patients.
- A **waterfall plot** to explain an individual prediction.

The SHAP explainer in the notebook uses the model's raw output, so the SHAP base values and feature contributions represent the model's raw score rather than direct probability values.

## Repository Structure

```text
diabetes-prediction-ml/
├── README.md
├── requirements.txt
├── .gitignore
└── diabetes_prediction.ipynb
```

## Installation and Usage

### Option 1: Google Colab

1. Open Google Colab.
2. Upload `diabetes_prediction.ipynb`.
3. Run the notebook cells from top to bottom.

The dataset is generated inside the notebook, so no external dataset download is required.

### Option 2: Local Environment

Clone the repository:

```bash
git clone https://github.com/<your-username>/diabetes-prediction-ml.git
cd diabetes-prediction-ml
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Then open the notebook using Jupyter Notebook or JupyterLab and run the cells in order.

## Technologies Used

- Python
- NumPy
- pandas
- Matplotlib
- Seaborn
- scikit-learn
- XGBoost
- LightGBM
- SHAP
- Jupyter / Google Colab

## Reproducibility

Fixed random seeds are used throughout the notebook where relevant, including data generation, train/test splitting, model training, and sampling. For the most consistent results, run the notebook from top to bottom in a clean environment.

## Git and Version Control

The repository follows basic Git best practices:

- Use clear and meaningful commit messages.
- Keep each commit focused on one logical change.
- Keep temporary files, cache files, and local environments out of the repository using `.gitignore`.
- Use `main` as the stable branch.
- Tag the completed project version, for example `v1.0.0`.

Example commit history:

```text
feat: add initial diabetes prediction notebook
feat: add data preprocessing and EDA
feat: add XGBoost and LightGBM models
feat: add model evaluation and SHAP explanations
docs: add project README
chore: add requirements and gitignore
```

Example release tag:

```bash
git tag -a v1.0.0 -m "First complete project release"
git push origin v1.0.0
```

## Limitations

- The dataset is synthetic and intended for learning and demonstration.
- The models are not validated on real clinical patient data.
- The dataset contains class imbalance, and no resampling technique is applied in the current notebook.
- Hyperparameters are manually selected rather than optimized through cross-validation.
- The project uses a single train/test split.
- The default classification threshold is used.
- SHAP explanations describe model behavior and should not be interpreted as medical causality.

## Future Improvements

Possible improvements include:

- Applying cross-validation and hyperparameter optimization.
- Testing class-weighting or resampling methods for class imbalance.
- Comparing additional machine learning models.
- Optimizing the classification threshold.
- Adding probability calibration.
- Validating the workflow using a real-world dataset.

## Training Program Acknowledgment

This project was developed as part of the **أساليب تعلم الآلة المتقدمة — Applied Machine Learning for Intelligent Systems** training program by **SDAIA Academy**.

Special thanks to SDAIA Academy for providing the training program and learning environment.

🔗 [SDAIA Academy on GitHub](https://github.com/SDAIAAcademy)

## Disclaimer

This project is for **educational purposes only** and is **not a medical diagnostic tool**.
