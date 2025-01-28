## 🔧 Project Overview

This project is designed to:

Ingest data, preprocess it, and engineer features for analysis.
Build and train machine learning models to predict wine quality.
Evaluate model performance with metrics and experiment tracking tools like MLflow and DagsHub.
Enable a seamless and automated pipeline, demonstrating the power of reproducibility in machine learning.

## 📚 Dataset
The Wine Quality Dataset contains chemical properties of red and white wines, along with quality ratings.
Key Features include:

Acidity levels
Sugar content
Alcohol percentage
Sulfates
Chlorides
... and more!
Target Variable: Wine quality, rated on a scale of 1–10.

## 🛠️ ML Pipeline Workflow

1. Data Ingestion
Load the dataset from a structured source for analysis and preprocessing.
Ensure data integrity and validation.

2. Data Transformation
Feature Engineering: Extract relevant features to improve predictive accuracy.
Data Preprocessing: Handle missing values, normalize/scale features, and encode categorical variables.

3. Model Training
Train machine learning models using algorithms like Random Forest, Gradient Boosting, and Logistic Regression.
Optimize model hyperparameters using the configurations defined in params.yaml.

4. Model Evaluation
Evaluate performance using metrics like accuracy, precision, recall, and F1 score.

Track experiments, hyperparameters, and model artifacts using MLflow and DagsHub.

## 🛠️ Project Workflows

To ensure modularity and scalability, the following steps were followed:

Update Configurations

config.yaml: Manages overall pipeline settings.
schema.yaml: Defines data schema and validation rules.
params.yaml: Contains hyperparameters for model training.
Define and Update Entities

Modular components like data loaders, transformers, and model trainers.
Build Pipeline Components

Code modular, reusable functions for ingestion, preprocessing, training, and evaluation.
Integrate the Pipeline

Combine all components into a cohesive pipeline for end-to-end execution.
Orchestrate with Main Script

main.py: Acts as the orchestrator to execute the ML pipeline seamlessly.

## ✨ Project Highlights

End-to-End Workflow: Covers everything from data ingestion to model evaluation.
Modular Design: Built for reusability, scalability, and ease of maintenance.
Experiment Tracking: Leveraged MLflow and DagsHub to track performance and maintain reproducibility.
Wine Quality Dataset: A popular dataset that allows for insightful feature engineering and predictive analysis.
