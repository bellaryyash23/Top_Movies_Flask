# 🎬Top Movies Website using HTML, CSS, Bootstrap, Requests API, SQLite & Flask of Python

🌟A website which allows users enlist their Top 10 Favourite Movies and along with that be able to add Review & Ratings to the respective movies. The users can use this
website to maintain their binge watch list and be able to update it to keep it relevant to them.

🌟The Front-end of the website is built using HTML, CSS & Bootstrap technologies along with that, Jinja templating is used across webpages. The Back-end of the website is 
hosted using the Flask server. This also uses other technologies like API request call, WTForms, etc. The website uses SQLite as Database and it is operated on the server
side using SQLAlchemy extension provided by Flask.

👉On the website, the enlisted movies are ranked on the basis of the rating provided by the user. The users can Add New Movies, Edit/ Update the review & rating of movie &
Delete/ Remove a movie from the list of movies. The final website is as follows:

![Top Movie Website](https://github.com/bellaryyash23/Top_Movies_Flask/blob/master/samples/site.gif?raw=true)

👆The TOP MOVIES WEBSITE👆

👉In the 'main.py' file, first the Flask app is setup for the website. Then the SQLite database 'movies.db' is created to store the movies data. The SQL structure is 
created using the SQLAlchemy extension provided by Flask. Initially a single movie data is added to the database for refernce.

👉The home route of website is setup using the Flask decorator functions and on this route the list of all the movies from the database along with their ranking is rendered 
onto the index.html file.

![Home Page of Website](https://github.com/bellaryyash23/Top_Movies_Flask/blob/master/samples/home.jpg?raw=true)

👆 Home Page of the Website👆

👉Next, inorder to edit the review & rating of the movies, an edit route is defined. On this route a WTForm is used to allow user to edit the respective fields. This 
updated data is the again updated in the database.

![Edit Page of Website](https://github.com/bellaryyash23/Top_Movies_Flask/blob/master/samples/edit.jpg?raw=true)

👆 Edit Page of the Website👆

👉Now, inorder for the user to remove a certain movie from the list of movies, the delete route is setup. The option to delete and remove a certain movie from the movies database
is provided on the home page itself. This deletion occurs using the id of the movie entry. The updated list with new rankings gets rendered again on the home route.

👉Finally inorder to add a new movie to the list of movies, we use the add route. On this route a WTForm is used to get the title of the movie to be added to the list.
Then using the 'Movie_DB' API, a GET request is made to acquire list of all movies matching that movie title.

👉This list of movies with their data links is then displayed on select page and depending on which movie link the user click, the respective data gets passed over to the
find route which again makes a api call to the 'Moive_DB' api but, this time with unique movie id passed as parameter.

👉All the data files created in the database are populated with the data acquired from the API call except for the review & rating to which the find route is redirected.
Once entered all the relevant data, the movie entry gets added to the database and consequently onto the website.

![Movie Addition Page of Website](https://github.com/bellaryyash23/Top_Movies_Flask/blob/master/samples/add.jpg?raw=true)

👆Enter Movie title to add to Movie List👆

![Selection Page for movie titles](https://github.com/bellaryyash23/Top_Movies_Flask/blob/master/samples/select.jpg?raw=true)

👆Select Movie from the list of Possisible Movies👆

👉The SQLite Database created has the following structure.

![Database of Website](https://github.com/bellaryyash23/Top_Movies_Flask/blob/master/samples/data.JPG?raw=true)

👆Database of the Website👆
