import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os

os.makedirs('models', exist_ok=True)

# Train URL Model
print("Training URL Model...")
df_url = pd.read_csv('data/PhishingURLs.csv')
X_url = df_url.drop(['url', 'label'], axis=1)
y_url = df_url['label']
X_train, X_test, y_train, y_test = train_test_split(X_url, y_url, test_size=0.2, random_state=42)

url_model = RandomForestClassifier(n_estimators=100, random_state=42)
url_model.fit(X_train, y_train)
url_acc = accuracy_score(y_test, url_model.predict(X_test))
joblib.dump(url_model, 'models/url_model.pkl')
print(f"✅ URL Model Accuracy: {url_acc:.3f}")

# Train Email Model
print("Training Email Model...")
df_email = pd.read_csv('data/Emails.csv')
X_email = df_email.drop(['text', 'label'], axis=1)
y_email = df_email['label']
X_train, X_test, y_train, y_test = train_test_split(X_email, y_email, test_size=0.2, random_state=42)

email_model = RandomForestClassifier(n_estimators=100, random_state=42)
email_model.fit(X_train, y_train)
email_acc = accuracy_score(y_test, email_model.predict(X_test))
joblib.dump(email_model, 'models/email_model.pkl')
print(f"✅ Email Model Accuracy: {email_acc:.3f}")
print("🎉 Models trained and saved!")
