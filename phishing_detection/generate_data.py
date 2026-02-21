import pandas as pd
import numpy as np
import os

os.makedirs('data', exist_ok=True)
np.random.seed(42)
n = 5000

# Generate Phishing URLs (5000 samples)
print("Generating URL dataset...")
url_data = []
for i in range(n):
    if np.random.rand() < 0.4:  # Phishing
        url = np.random.choice([
            f"http://192.168.{np.random.randint(1,255)}.{np.random.randint(1,255)}/login",
            f"https://{np.random.choice(['paypal','bank','secure'])}-login.com/verify",
            f"http://bit.ly/{np.random.randint(1000,9999)}",
            f"http://fake-{np.random.choice(['amazon','google','netflix'])}.com"
        ])
        label = 1
    else:  # Legit
        url = np.random.choice([
            "https://google.com", "https://github.com", "https://amazon.com",
            "https://stackoverflow.com", "https://youtube.com"
        ])
        label = 0
    
    features = {
        'url': url, 'label': label,
        'length': len(url)/100,
        'has_ip': 1 if '192.168' in url else 0,
        'suspicious_count': sum(1 for w in ['login','verify','secure','bank'] if w in url.lower()),
        'redirects': 1 if 'bit.ly' in url else 0,
        'abnormal_chars': len([c for c in url if c in '-_.'])
    }
    url_data.append(features)

pd.DataFrame(url_data).to_csv('data/PhishingURLs.csv', index=False)

# Generate Emails (5000 samples)
print("Generating Email dataset...")
email_data = []
phishing_kws = ['urgent', 'verify', 'password', 'suspended', 'click here']
for i in range(n):
    if np.random.rand() < 0.4:
        text = f"{np.random.choice(phishing_kws)}! Click here: http://fake.com"
        label, kw_count = 1, 2
    else:
        text = "Thanks for your purchase. Visit legit.com"
        label, kw_count = 0, 0
    
    features = {
        'text': text, 'label': label,
        'keyword_count': kw_count,
        'urgency_score': np.random.uniform(0.8 if label else 0.1),
        'link_count': 1 if label else 0
    }
    email_data.append(features)

pd.DataFrame(email_data).to_csv('data/Emails.csv', index=False)
print("✅ Datasets created! (5000 samples each)")
