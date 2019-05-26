# -*- coding: utf-8 -*-

from urllib.parse import urljoin
from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
import os
import json

url = 'https://www.eventpop.me/g/entertainment'

headers = {
    'User-Agent': '01204499',
    'From': 'Anongnat.rat@ku.ac.th'
}

def get_page(url) :
	global headers
	text = ''
	try :
		r = requests.get(url,headers=headers,timeout=2)
		text = r.text
	except (KeyboardInterrupt, SystemExit):
		raise
	except :
		print("GET PAGE ERROR!")
	return text

cannot_mk_dir_list = ['|', '\\', '/', ':', '?', '<', '>', '\'', '\"']

out_dir = './source'
if not os.path.exists(out_dir) :
	os.mkdir(out_dir)

raw_html = get_page(url)
# print(raw_html)
soup = BeautifulSoup(raw_html, 'html.parser')

soup = soup.find('section', id='events')
for div_soup in soup.find_all('div', {'class':'col-md-4 col-sm-6 col-xs-12'}) :
	title_soup = div_soup.find('strong', {'class':'text-default'})
	title = title_soup.get_text('strong')
	print(title)
	rename_title = title
	for symbol in cannot_mk_dir_list :
		rename_title = rename_title.replace(symbol, '')

	concert_path = f'{out_dir}/{rename_title}'
	if not os.path.exists(concert_path) :
		os.mkdir(concert_path)

	img_soup = div_soup.find('img')
	link = img_soup.get('src')
	# urlretrieve(link, f"{concert_path}/img.jpg")

	date_soup = div_soup.find('div', {'class':'hidden-md hidden-lg'})
	date = date_soup.get_text('div')
	print(date)

	detail = {}
	detail['title'] = title 
	detail['date'] = date
	# record[] = ....
	with open(f'{concert_path}/detail.json', 'w') as outfile:  
		json.dump(detail, outfile)