from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv("data/raw/fed_spending.csv")
    data = df.to_dict(orient="records")
    return render_template("index.html", data=data, tableau_url="https://public.tableau.com/views/fed_spending/Sankey_View")

if __name__ == "__main__":
    app.run(debug=True)