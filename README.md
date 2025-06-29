# TrafficTelligence-Advanced-Traffic-Volume-Estimation-with-ML

> **TrafficTelligence 🚦 — Smarter roads, better cities.**

TrafficTelligence is a Flask-based machine learning web app that predicts real-time traffic volume using environmental and time data inputs. Built with Python, scikit-learn, and Flask, it helps commuters and city planners make smarter traffic decisions.
# 🚦 TrafficTelligence

**Advanced Traffic Volume Estimation with Machine Learning**

---

## 📌 Project Description

**TrafficTelligence** is a smart, ML-powered web application that predicts real-time traffic volume based on weather, holidays, and time-based features. Built using **Python** and **Flask**, it empowers commuters, traffic authorities, and city planners to make data-driven traffic flow decisions.

---

## 📚 Table of Contents

- [✨ Features](#-features)
- [⚙️ Installation](#️-installation)
- [🗂️ Project Structure](#️-project-structure)
- [🚀 Usage](#-usage)
- [🔗 API Reference](#-api-reference)
- [📬 Contact](#-contact)

---

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
|   ├── column.pkl
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

Visit: [http://127.0.0.1:5001](http://127.0.0.1:5001) to open the app in your browser.

### 📸 Screenshots

\
*Clean traffic input form with custom background.*
![Screenshot 2025-06-29 195057](https://github.com/user-attachments/assets/70f09a86-4300-49fd-98c2-86ce9fdf71d6)
![Screenshot 2025-06-29 195129](https://github.com/user-attachments/assets/d22b68f1-af27-4a97-ac8f-aa113e9764a0)

\
*Animated output page with prediction result.*
![Screenshot 2025-06-29 195156](https://github.com/user-attachments/assets/b2ac6c2b-8767-4125-8a8d-915168098ba1)

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

---

## 🤝 Contributing

Contributions are welcome!\
To contribute:

1. **Fork** this repository.
2. Create a **feature branch**:
   ```bash
   git checkout -b feature-branch
   ```
3. **Commit** your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push** to your fork:
   ```bash
   git push origin feature-branch
   ```
5. Submit a **Pull Request** 

## 📬 Contact

**Author:** Chebathina Anjali\
**GitHub:** [anjalichebathina](https://github.com/anjalichebathina)

---

> **TrafficTelligence 🚦 — Smarter roads, better cities.**

