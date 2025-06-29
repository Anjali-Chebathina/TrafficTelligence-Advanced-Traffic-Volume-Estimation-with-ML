# 🚦 TrafficTelligence

**Advanced Traffic Volume Estimation with Machine Learning**

---

## 📌 Project Description

**TrafficTelligence** is a smart, ML-powered web application that predicts real-time traffic volume based on weather, holidays, and time-based features. Built using **Python** and **Flask**, it empowers commuters, traffic authorities, and city planners to make data-driven traffic flow decisions.

## ✨ Features

- ✅ Real-time traffic volume prediction using a regression model
- ✅ Clean, user-friendly web form with smart input validations
- ✅ Animated output page for engaging result display
- ✅ Modular Flask backend for easy deployment and scaling

---

## ⚙️ Installation

### 🔑 Pre-requisites

- **Python 3.8+**
- **pip** (Python package manager)
- **Virtualenv** (optional, but recommended)

### 🚦 Setup Steps

```bash
# Clone this repository
git clone https://github.com/anjalichebathina/TrafficTelligence.git

# Navigate to the project folder
cd TrafficTelligence_Project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Or activate on Mac/Linux
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt
```

---

## 🗂️ Project Structure

```
TrafficTelligence_Project/
├── Flask/
│   ├── app.py
│   ├── model.pkl
│   ├── encoder.pkl
│   ├── static/
│   │   └── bg.png
│   └── templates/
│       ├── index.html
│       └── output.html
└── requirements.txt
```

---

## 🚀 Usage

### ✅ Start the Flask App

```bash
# Navigate to the Flask app directory
cd Flask

# Run the Flask server
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000) to open the app in your browser.

### 📸 Screenshots

\
*Clean traffic input form with custom background.*

\
*Animated output page with prediction result.*

---

## 🔗 API Reference

| Endpoint   | Method | Description                              |
| ---------- | ------ | ---------------------------------------- |
| `/`        | GET    | Display input form page                  |
| `/predict` | POST   | Process input data and return prediction |

**Sample Response:**

```json
{
  "prediction": "Estimated Traffic Volume is: 4215 units"
}
```



## 📬 Contact

**Author:** Chebathina Anjali\
**GitHub:** [anjalichebathina](https://github.com/anjalichebathina)

---

> **TrafficTelligence 🚦 — Smarter roads, better cities.**

