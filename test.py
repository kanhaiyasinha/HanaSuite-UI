from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('finalDashBoard1.html')

@app.route('/system_info')
def system_info():
    # Read the Excel file into a Pandas DataFrame
    path = os.getcwd()
    excel_file = os.path.join(path, 'system_overview.xlsx')  # Replace 'your_excel_file.xlsx' with your actual file path
    df = pd.read_excel(excel_file)

    # Render the HTML template with the DataFrame
    return render_template('data99.html', data=df.to_html(index=False))

if __name__ == '__main__':
    app.run(debug=True, port=8080)