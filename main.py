from flask import Flask, render_template, request, url_for, redirect
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'



class SearchByPostCode(FlaskForm):
    code = StringField('Enter Post Code', validators=[DataRequired()])
    submit = SubmitField('Search')


@app.route("/", methods=['GET', 'POST'])
def home():
    form = SearchByPostCode()
    if form.validate_on_submit():
        return redirect(url_for('restaurants', code=request.form['code']))

    return render_template("index.html", form=form)


@app.route("/restaurants", methods=['GET', 'POST'])
def restaurants():
    postcode = "EC4M7RF"
    url = f"https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/{postcode}"

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # raises exception when not a 2xx response
    restaurants = response.json()["restaurants"][:10]

    return render_template('restaurants.html', restaurants=restaurants)


if __name__ == '__main__':
    app.run(debug=True)