import subprocess
import sys
import os

print("🚀 PhishGuard AI - Starting up...")
print("=" * 50)

# Step 1: Generate data
print("📊 Step 1/3: Generating training data...")
subprocess.run([sys.executable, 'generate_data.py'])

# Step 2: Train models
print("🤖 Step 2/3: Training ML models...")
subprocess.run([sys.executable, 'train.py'])

# Step 3: Start web server
print("🌐 Step 3/3: Starting web server...")
print("✅ Open your browser to: http://127.0.0.1:5000")
print("✅ Press Ctrl+C to stop")
os.system(f"{sys.executable} app.py")
