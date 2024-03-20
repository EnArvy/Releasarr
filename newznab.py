import requests
from config import newznaburl, newznabkey, Preferred, Excluded
from tmdb import get_movie, get_tv

def sizeof_fmt(num, suffix="B"):
    num = int(num)
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f} {unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def get_movie_releases(movieid):
	global newznaburl
	if newznaburl.endswith('/'):
		newznaburl = newznaburl[:-1]
	if not newznaburl.endswith('/api'):
		newznaburl = newznaburl + '/api'
	movieid = get_movie(movieid)['imdb_id']
	response = requests.get(url=f'{newznaburl}/?t=movie&apikey={newznabkey}&extended=1&imdbid={movieid}&o=json')
	releases = []
	releasesBest = []
	for item in response.json()['channel']['item']:
		if prefered(item['title']) and not excluded(item['title']):
			releasesBest.append({
				'title': item['title'],
				'size': int(item['enclosure']['@attributes']['length']),
				'link': item['link'],
				'id' : item['guid']
			})
		elif not excluded(item['title']):
			releases.append({
				'title': item['title'],
				'size':int(item['enclosure']['@attributes']['length']),
				'link': item['link'],
				'id' : item['guid']
			})
	releasesBest.sort(key=lambda x: x['size'])
	releases.sort(key=lambda x: x['size'])
	releasesBest.extend(releases)
	releasesBest = releasesBest[:30]
	for release in releasesBest:
		release['size'] = sizeof_fmt(release['size'])
	return releasesBest


def get_tv_releases(tvid):
	global newznaburl
	if newznaburl.endswith('/'):
		newznaburl = newznaburl[:-1]
	if not newznaburl.endswith('/api'):
		newznaburl = newznaburl + '/api'
	tvid = get_tv(tvid)['external_ids']['imdb_id']
	print(tvid)
	response = requests.get(url=f'{newznaburl}/?t=tvsearch&apikey={newznabkey}&extended=1&imdbid={tvid}&o=json')
	releases = []
	releasesBest = []
	for item in response.json()['channel']['item']:
		if prefered(item['title']) and not excluded(item['title']):
			releasesBest.append({
				'title': item['title'],
				'size': int(item['enclosure']['@attributes']['length']),
				'link': item['link'],
				'id' : item['guid']
			})
		elif not excluded(item['title']):
			releases.append({
				'title': item['title'],
				'size':int(item['enclosure']['@attributes']['length']),
				'link': item['link'],
				'id' : item['guid']
			})
	releasesBest.sort(key=lambda x: x['size'])
	releases.sort(key=lambda x: x['size'])
	releasesBest.extend(releases)
	releasesBest = releasesBest[:30]
	for release in releasesBest:
		release['size'] = sizeof_fmt(release['size'])
	return releasesBest

def prefered(name:str) -> bool:
	words = name.lower().replace('.', ' ').split()
	for word in words:
		if word in Preferred:
			return True
def excluded(name:str) -> bool:
	words = name.lower().replace('.', ' ').split()
	for word in words:
		if word in Excluded:
			return True
		
def search(query:str):
	global newznaburl
	if newznaburl.endswith('/'):
		newznaburl = newznaburl[:-1]
	if not newznaburl.endswith('/api'):
		newznaburl = newznaburl + '/api'
	response = requests.get(url=f'{newznaburl}/?t=search&apikey={newznabkey}&extended=1&q={query}&o=json')
	results = []
	for item in response.json()['channel']['item']:
		results.append({
			'title': item['title'],
			'size': int(item['enclosure']['@attributes']['length']),
			'link': item['link'],
			'id' : item['guid']
		})
	return results

