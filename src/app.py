from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Path relative to Heroku root (../data/raw/ from src/)
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data/raw/fed_spending.csv"))
    data = df.to_dict(orient="records")
    return render_template("index.html", data=data, tableau_url="https://public.tableau.com/views/fed_spending/Sankey_View")

if __name__ == "__main__":
    app.run(debug=True)