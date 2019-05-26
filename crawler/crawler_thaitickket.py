# -*- coding: UTF-8 -*-
import codecs
from urllib.parse import urljoin
from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
import os
import json

url = 'http://www.thaiticketmajor.com/concert/'

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
	return text.lower()

cannot_mk_dir_list = ['\\', '/', ':', '?', '<', '>', '\'', '\"']

out_dir = './source'
if not os.path.exists(out_dir) :
	os.mkdir(out_dir)

raw_html = get_page(url)
# print(raw_html)
soup = BeautifulSoup(raw_html, 'html.parser')
soup = soup.find('section',  {'class':'section-event'})
#print(soup)
for li_soup in soup.find_all('div', {'class':'col-4 col-md-3 col-lg-2'}) :
	#print(li_soup)
	detail_soup = li_soup.find('div',{'class':'box-txt'} )
	#print(detail_soup)
	title_soup = detail_soup.find('a',{'class':'title'})
	#print(title_soup)
	title = title_soup.get_text('title')
	#print(title)
	rename_title = title
	for symbol in cannot_mk_dir_list :
		rename_title = rename_title.replace(symbol, '')

	concert_path = f'{out_dir}/{rename_title}'
	if not os.path.exists(concert_path) :
		os.mkdir(concert_path)

	pic_soup = li_soup.find('a', {'class':'box-img'})
	#print(pic_soup)
	img_soup = pic_soup.find('img')
	#print(img_soup)
	link = img_soup.get('data-src')
	print(link)

	urlretrieve('http://www.thaiticketmajor.com'+link, f"{concert_path}/img.jpg")

	date_soup = detail_soup.find('span')
	#print(date_soup)
	date = date_soup.get_text('span')
	print(date)
	
	detail = {}
	detail['title'] = title 
	detail['date'] = date
	# record[] = ....
	with codecs.open(f'{concert_path}/detail.json', 'w','utf-8') as outfile:  
		json.dump(detail, outfile,ensure_ascii=False)