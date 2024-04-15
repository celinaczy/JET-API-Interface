from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    postcode = "EC4M7RF"
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # raises exception when not a 2xx response
    restaurants = response.json()["restaurants"][:10]

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)