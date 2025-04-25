# 🏨 MLOps-Hotel-Revenue-Management-System

### A Predictive Analytics System for Hotel Reservation Status using MLOps Best Practices

## 📖 Project Description

The MLOps-Hotel-Revenue-Management-System is a machine learning application that predicts hotel booking cancellation status based on historical reservation data. This system aids revenue managers and hospitality stakeholders in improving booking forecasts, optimizing overbooking strategies, and enhancing customer retention by identifying potential cancellations before they occur.

This project simulates a real-world hotel revenue management workflow by incorporating:

- End-to-end MLOps pipeline for data ingestion, processing, model training, evaluation, and deployment.

- A LightGBM classification model optimized for performance on imbalanced booking data.

- MLFlow for experiment tracking and model registry.

- A Flask-based frontend for real-time inference, allowing hotel managers to input reservation details and receive booking status predictions.

## 🚀 Features
- **Data Pipeline:** Automated ingestion, preprocessing, label encoding, skewness handling, and feature selection.

- **ML Model:** LightGBM classifier with hyperparameter tuning and evaluation metrics (Accuracy, Precision, Recall, F1 Score).

- **MLFlow Integration:** Experiment tracking, metric logging, model registry.

- **Flask Frontend:** User-friendly web interface for making real-time predictions.

## 🧩 Use Case: Hotel Revenue Management

In the hospitality industry, booking cancellations significantly impact revenue forecasting and operational efficiency. This system empowers revenue managers to:

1. Predict cancellations preemptively based on key booking attributes (lead time, room type, market segment, etc.).

2. Implement proactive retention strategies (e.g., targeted offers, confirmations) for bookings likely to be canceled.

3. Optimize room allocation and overbooking policies to maximize occupancy rates while minimizing revenue loss.

4. Integrate with existing hotel management systems through APIs for scalable deployment.

## ⚙️ Tech Stack

Component | Tool/Technology
Data Processing | Pandas, NumPy
Modeling | LightGBM (Classification)
MLOps & Tracking | MLFlow
Web Framework | Flask
Frontend | HTML, CSS

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/MLOps-Hotel-Revenue-Management.git
cd MLOps-Hotel-Revenue-Management
```

## 2️⃣ Set Up the Environment

```
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
## 3️⃣ Run the Flask Application
```
python app.py
Visit: http://localhost:8080 (or the port configured).
```

## 🖥️ How to Use

1. Open the web interface via your browser.

2. Input reservation details:

3. Lead time, special requests, market segment, meal plan, room type, etc.

4. Submit the form.

5. View prediction: The system predicts whether the reservation is likely to be Canceled or Not_Canceled.
