from flask import Flask, render_template, request, send_from_directory
import os
from newznab import *
from tmdb import *
from download import *
from flask_httpauth import HTTPDigestAuth
from config import users, port, secret_key

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
auth = HTTPDigestAuth()



@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def home():
	if request.method == 'POST':
		query = request.form['query']
		category = request.form['cat']
		if category == 'movie':
			results = search_movie(query)
			return render_template('results.html', results=results, query=query, type='movie')
		elif category == 'tv':
			results = search_tv(query)
			return render_template('results.html', results=results, query=query, type='tv')
		else:
			results = search(query)
			return render_template('results.html', results=results, query=query, type='all')
	return render_template('home.html', movies = popular_movies(), tvs = popular_tv())

@app.route('/movie/<id>', methods=['GET'])
@auth.login_required
def movie(id):
	info = get_movie(id)
	releases = get_movie_releases(id)
	return render_template('releases.html', releases=releases, info=info)

@app.route('/tv/<id>', methods=['GET'])
@auth.login_required
def tv(id):
	info = get_tv(id)
	releases = get_tv_releases(id)
	return render_template('releases.html', releases=releases, info=info)

@app.route('/download/<id>', methods=['GET'])
@auth.login_required
def download(id):
	response = add_nzb(id)
	return response

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
	if __name__ == "__main__":
		from waitress import serve
		serve(app, host="0.0.0.0", port=port)
