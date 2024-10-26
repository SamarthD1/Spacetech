from flask import Flask, render_template, request
import pandas as pd


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/segments', methods=['POST'])
def segments():
    # Logic to show segments based on uploaded data
    # For simplicity, we'll load the segmented data
    #segmented_data = pd.read_csv('../data/segmented_customers.csv')
    segmented_data = pd.read_csv('data:/segmented_customers.csv')
    return render_template('segments.html', tables=[segmented_data.to_html(classes='data')], titles=segmented_data.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
