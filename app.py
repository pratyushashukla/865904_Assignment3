import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/countryDetails", methods=['POST'])
def countryDetails():
    base_url = "https://restcountries.com/v3.1/name/"
    selectedCountry = request.form['country']
    print(selectedCountry)
    url = f"{base_url}{selectedCountry}"
    response = requests.get(url)

    if response.status_code == 200:
        country_details = response.json()

        if country_details:
            return render_template("country_Details.html", country_details=country_details)
        else:
            return "Error: Empty response"
    else:
        return f"Error: Unable to fetch data. Status code: {response.status_code}"

if __name__ == "__main__":
    app.run(debug=True)
