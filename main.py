import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

MOVIE_DB_API_KEY = os.environ.get('MOVIE_DB_API_KEY')

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
Bootstrap(app)
db = SQLAlchemy(app)


class EditForm(FlaskForm):
    new_rating = StringField("Your rating: (e.g: 7.5)", validators=[DataRequired(message="This field is required.")])
    new_review = StringField("Your review: ", validators=[DataRequired("This field is required.")])
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired(message="This field is required.")])
    submit = SubmitField("Add Movie")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(1000), nullable=False)


# db.create_all()

new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)

# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    movie_selected = Movie.query.get(movie_id)
    if form.validate():
        movie_selected.rating = form.new_rating.data
        movie_selected.review = form.new_review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie_selected, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_selected = Movie.query.get(movie_id)
    db.session.delete(movie_selected)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate():
        movie_title = form.movie_title.data
        parameters = {
            "api_key": MOVIE_DB_API_KEY,
            "query": movie_title
        }
        response = requests.get(url="https://api.themoviedb.org/3/search/movie", params=parameters)
        results = response.json()["results"]
        movie_data = [{"movie_title": movie['title'], "movie_year": movie['release_date'], "movie_id": movie['id']} for
                      movie in results]
        return render_template("select.html", movies=movie_data)
    return render_template("add.html", form=form)


@app.route("/find")
def find():
    movie_id = request.args.get("id")
    parameters = {
        "api_key": MOVIE_DB_API_KEY,
    }
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}", params=parameters)
    movie_data = response.json()
    new_entry = Movie(
        title=movie_data["title"],
        year=movie_data["release_date"].split("-")[0],
        img_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}",
        description=movie_data["overview"]
    )
    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for("edit", id=new_entry.id))


if __name__ == '__main__':
    app.run(debug=True)
