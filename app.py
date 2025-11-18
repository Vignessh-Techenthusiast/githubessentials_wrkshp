# app.py
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def create_sample_dataframe():
    """Creates a small pandas DataFrame."""
    data = {
        'Product': ['Laptop', 'Keyboard', 'Mouse', 'Monitor'],
        'Price': [1200, 75, 25, 300],
        'InStock': [True, True, False, True]
    }
    df = pd.DataFrame(data)
    return df

@app.route('/')
def index():
    # 1. Create the DataFrame
    df = create_sample_dataframe()
    
    # 2. Convert the DataFrame to an HTML table string
    #    The 'to_html()' method is the easiest way to display a DF in Flask.
    #    It creates the <table>...</table> source code.
    df_html = df.to_html(index=False, classes='table table-striped')
    
    # 3. Pass the HTML string to the template
    return render_template('display_data.html', table_html=df_html)

if __name__ == '__main__':
    # You must have pandas installed: pip install pandas flask
    app.run(debug=True)
