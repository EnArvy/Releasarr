import requests
from config import sabnzbdurl, sabnzbdkey, newznaburl, newznabkey, sabcat
from urllib.parse import quote_plus
import json

def add_nzb(id):
	global newznaburl
	if newznaburl.endswith('/'):
		newznaburl = newznaburl[:-1]
	if not newznaburl.endswith('/api'):
		newznaburl = newznaburl + '/api'
	response = requests.get(url=f'{newznaburl}/?t=get&id={id}&apikey={newznabkey}')
	nzburl = newznaburl + '?t=get&id=' + id + '&apikey=' + newznabkey
	response = requests.get(url=f"{sabnzbdurl}/api?mode=addurl&apikey={sabnzbdkey}&name={quote_plus(nzburl)}&cat={sabcat}")
	res = response.content.decode('utf-8').replace("'", '"').lower()
	res = json.loads(res)
	if res['nzo_ids'] is not None:
		return '<body><h1>Download added to queue</h1></body>'
	else:
		return '<body><h1>Failed to add download to queue</h1></body>'
