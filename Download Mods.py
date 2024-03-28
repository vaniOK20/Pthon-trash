import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
page = 0
mods = []
used_mod = None
search_word = None

def get_mods(url):
	if url.endswith("mods"):
		if not page==0:
			url = url+f'?o={page*10*2}'
			if not search_word is None:
				url = url+f'&q={search_word}'
		if url.endswith("mods") and not search_word is None:
			url = url+f'?q={search_word}'
	try:
		response = requests.get(url, headers=headers)
		response.raise_for_status()
		return response.text
	except requests.RequestException as e:
		print("Error fetching URL:", e)
		return None

def parse_html(html):
	global mods
	mods = []
	soup = BeautifulSoup(html, 'html.parser')
	mod_cards = soup.find_all('article', class_='project-card')
	for mod_card in mod_cards:
		title = mod_card.find('h2', class_='name').text
		description = mod_card.find('p', class_='description').text
		url = mod_card.find('a', class_='gallery').get('href')
		mods.append((title, description, url[url.find("d/")+2:]))
	clear()

def parse_versions(html):
	version_title = []
	soup = BeautifulSoup(html, 'html.parser')
	version_cards = soup.find_all('div', class_='featured-version button-transparent')
	for version_card in version_cards:
		version_title_element = version_card.find('a', class_='top')
		version_game = version_card.find('div', class_='game-version item').text
		if version_title_element is not None:
			version_title.append((version_title_element.text, 'https://modrinth.com'+version_title_element.get('href'), version_game))
	i=0
	while not len(version_title)==int(i):
		print(f'[{i+1}][{version_title[i][2]}]:          {version_title[i][0]}')
		i=i+1
	version_mod = input()
	if not int(version_mod)==0:
		html=get_mods(version_title[int(version_mod)-1][1])
		download(html)
		used_mod = None

def download(html):
	soup = BeautifulSoup(html, 'html.parser')
	download_button = soup.find('div', class_='file primary')
	response=requests.get(download_button.find('a').get('href'))
	with open(f'{download_button.text[:str(download_button.text).find(".jar")]}.jar', 'wb') as file:
		file.write(response.content)
	os.system('cls')
	html=get_mods('https://modrinth.com/mods')
	parse_html(html)

def clear():
	os.system('cls')
	i=0
	while not len(mods)==int(i):
		print(f'[{i+1}]{mods[i][0]}')
		i=i+1

def update():
	html = get_mods('https://modrinth.com/mods')
	parse_html(html)

update()

while True:
	mod=input()
	if mod=='next page':
		page=page+1
		update()
	elif mod=='back page' and page>0:
		page=page-1
		update()
	elif mod=='download':
		if used_mod:
			html = get_mods(f'https://modrinth.com/mod/{used_mod}/versions')
			parse_versions(html)
		else:
			print('You not choised the mod')
	elif mod.startswith("search:"):
		search_word = mod[7:]
		page=0
		update()
	else:
		if int(mod)<=len(mods):
			print(f"Title: {mods[int(mod)-1][0]}\nDescription: {mods[int(mod)-1][1]}")
			used_mod=str(mods[int(mod)-1][2])