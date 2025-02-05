# app.py
from flask import Flask, render_template, request
import requests
import json
from markupsafe import escape

app = Flask(__name__)

# Neon-themed data loading
def load_data():
    url = "https://raw.githubusercontent.com/MarwanRTX/Chatbots-Projects/refs/heads/main/ChatBot%20Choices%20based%20on%20web%20file/prices.json"
    try:
        response = requests.get(url)
        return json.loads(response.text)
    except Exception as e:
        print(f"Exception : {e}")

data = load_data()

@app.route('/', methods=['GET', 'POST'])
def home():
    response_items = None
    selected_category = None
    
    if request.method == 'POST':
        selected_category = escape(request.form.get('category'))
        if selected_category in data:
            response_items = data[selected_category]
    
    return render_template(
        'index.html',
        categories=data.keys(),
        response_items=response_items,
        selected_category=selected_category
    )

if __name__ == '__main__':
    app.run(debug=True)