# Phishing-Detection-Website-
PhishGuard AI-Phishing Detection This website is created to detect any phishing activity in URLs and Emails

**PROBLEM STATEMENT**: Develop an AI-based system that detects phishing emails/URLs in real-time and alerts users

Phishing attacks increased 58% in 2025 causing $52B in global losses. Current solutions fail because:
**Traditional filters miss 40% of phishing** (zero-day attacks)  
**No real-time user feedback** (click before warning)  
**Poor UX**(boring interfaces, no urgency)  
**Mobile blindness** (60% attacks via mobile)  
**No multi-channel detection** (URL + email gaps)

**Solution Approach** : Hybrid ML + Rule-Based Architecture
1.Rule-Based Approach
500+ keywords: login, verify, urgent, winner, suspended
Pattern matching: IP addresses, typosquatting (paypa1.com)
Path analysis: /admin, /login, /secure
Threshold: Score > 35pts = PHISHING!

**Tech Stack Used**
Backend: Flask 2.3.3 (REST API)
ML: Scikit-learn 1.3.2 + Joblib (hybrid models)
Frontend: HTML5 + CSS3 + Vanilla JS (50KB)
Notifications: Web Notification API + Vibration
Audio: Web Audio API (custom siren)
Animations: CSS @keyframes (60fps GPU accelerated)
Responsive: CSS Grid + Mobile-first design

**Setup Instructions**
# 1. Clone + Install
git clone https://github.com/amulyaM6/Phishing-Detection-Website-.git
cd PhishGuard-AI
pip install -r requirements.txt

# 2. First-time model training
python train.py

# 3. Start server
python app.py
Open: http://127.0.0.1:5000

**Test Cases** 
PHISHING DETECTION 
(EMAILS)
**Input	                        Expected**	
Thanks for purchase	            SAFE 1%
URGENT: Account suspended!	    PHISH 97%	
Winner! Free iPhone!	          PHISH 96%

(URLs)
**Input	                       Expected**	
https://google.com	           SAFE 2%	
http://192.168.1.1/admin       PHISH 98%
hey	                           INVALID URL



