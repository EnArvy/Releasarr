import requests
from config import tmdbkey
import time

tmdburl = 'https://api.themoviedb.org/3'

def search_movie(movie_name: str) -> list:
	response = None
	while response is None:
		try:
			time.sleep(0.5)
			print('Searching for ' + movie_name)
			response = requests.get(url=tmdburl + '/search/movie?api_key=' + tmdbkey + '&query=' + movie_name)
		except:
			pass
	results = []
	for item in response.json()['results']:
		if item['poster_path'] is not None:
			results.append({
				'title': item['title'],
				'id': item['id'],
				'rating': item['vote_average'], 
				'popularity': item['popularity'], 
				'poster': 'https://image.tmdb.org/t/p/w500' + item['poster_path'], 
				'overview': item['overview'],
				'year': item['release_date'][:4]
			})
			print(item['id'])
		if len(results) == 15:
			break
	return results

def search_tv(tv_name: str) -> list:
	response = None
	while response is None:
		try:
			time.sleep(0.5)
			print('Searching for ' + tv_name)
			response = requests.get(url=tmdburl + '/search/tv?api_key=' + tmdbkey + '&query=' + tv_name)
		except:
			pass
	results = []
	for item in response.json()['results']:
		if item['poster_path'] is not None:
			results.append({
				'title': item['name'],
				'id': item['id'],
				'rating': item['vote_average'], 
				'popularity': item['popularity'], 
				'poster': 'https://image.tmdb.org/t/p/w500' + item['poster_path'], 
				'overview': item['overview'],
				'year': item['first_air_date'][:4]
			})
		if len(results) == 15:
			break
	return results

def get_tv(tv_id:str):
	response = None
	while response is None:
		try:
			time.sleep(0.5)
			print('Searching for ' + tv_id)
			response = requests.get(url=tmdburl + '/tv/' + str(tv_id) + '?api_key=' + tmdbkey + '&append_to_response=external_ids')
		except:
			pass
	return response.json()

def get_movie(movie_id: str) -> dict:
	response = None
	while response is None:
		try:
			time.sleep(0.5)
			print('Searching for ' + movie_id)
			response = requests.get(url=tmdburl + '/movie/' + str(movie_id) + '?api_key=' + tmdbkey)
		except:
			pass
	return response.json()

def popular_movies():
	response = None
	while response is None:
		try:
			time.sleep(0.5)
			print('Getting popular movies')
			# response = requests.get(url=tmdburl + '/movie/popular?api_key=' + tmdbkey)
			response = requests.get(url=tmdburl + '/discover/movie?api_key=' + tmdbkey + '&watch_region=US&with_watch_providers=2|3|7|8|9|10|11|15')
		except:
			pass
	results = []
	for item in response.json()['results']:
		if item['poster_path'] is not None:
			results.append({
				'title': item['title'],
				'id': item['id'],
				'rating': item['vote_average'], 
				'popularity': item['popularity'], 
				'poster': 'https://image.tmdb.org/t/p/w500' + item['poster_path'], 
				'overview': item['overview'],
				'year': item['release_date'][:4]
			})
		if len(results) == 6:
			break
	return results

def popular_tv():
	response = None
	while response is None:
		try:
			time.sleep(0.5)
			print('Getting popular tv')
			response = requests.get(url=tmdburl + '/discover/tv?api_key=' + tmdbkey+ '&watch_region=US&with_watch_providers=2|3|7|8|9|10|11|15')
		except:
			pass
	results = []
	for item in response.json()['results']:
		if item['poster_path'] is not None:
			results.append({
				'title': item['name'],
				'id': item['id'],
				'rating': item['vote_average'], 
				'popularity': item['popularity'], 
				'poster': 'https://image.tmdb.org/t/p/w500' + item['poster_path'], 
				'overview': item['overview'],
				'year': item['first_air_date'][:4]
			})
		if len(results) == 6:
			break
	return results