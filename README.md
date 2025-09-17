# 🚨 Brute Force Login Detector

## 📌 Overview
This project is a **Flask-based login system** with a **log monitoring script** that detects brute-force login attempts.  

It simulates multiple failed login attempts, tracks suspicious IPs, and flags them once a threshold is exceeded.  

🔐 Designed for **resume building**, **GitHub portfolio**, and practicing **IDS/IPS concepts**.

---

## ⚙️ Features
- 🔑 Simple **Flask login system** (`app.py`)
- 📜 Logs all login attempts (success & failure)
- 👀 **Detector script (`detector.py`)** monitors logs in real-time
- 🚨 Detects brute-force attempts (e.g., >3 failed logins)

---

## 🛠️ Tech Stack
- Python 3
- Flask
- Logging module

---

## 🚀 Getting Started

Step 1. Clone the Repository
```bash
git clone https://github.com/your-username/brute-force-detector.git
cd brute-force-detector
```

Step 2. Create a Virtual Environment
```bash
python3 -m venv venv
```
Activate (Linux/Mac):
```bash
source venv/bin/activate
```
Activate (Windows):
```bash
venv\Scripts\activate
```
Step 3. Install Dependencies
```bash
pip install -r requirements.txt
```
Step 4. Run the Flask App
```bash
python app.py
```

➡ Open in browser: http://localhost:5000

Step 5. Run the Detector
```bash
python detector.py
```
