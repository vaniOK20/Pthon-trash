import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk
from bs4 import BeautifulSoup
import io
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
page = 0
mods = []
search_word = None
versions = False
images_dict = {}

def wrap_text(text, max_width, font):
	lines = []
	line = ''
	for word in text.split():
		if font.measure(line + word) < max_width:
			line += word + ' '
		else:
			lines.append(line)
			line = word + ' '
	lines.append(line)
	return lines

def get_mods(url):
	global page, search_word
	if url.endswith("mods"):
		if not page == 0:
			url = url+f'?o={page*10*2}'
			if search_word is not None:
				url = url+f'&q={search_word}'
		if url.endswith("mods") and search_word is not None:
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
		icon = mod_card.find('a', class_='icon').find('img').get('src')
		url = mod_card.find('a', class_='gallery').get('href')
		mods.append((title, description, icon, url[url.find("d/")+2:]))
	for i, mod in enumerate(mods):
		slot(20, i*120+20, 480, i*120+130, mod[2], mod[0], mod[1])

def slot(x, y, x2, y2, img_url, text, description):
	global images_dict
	c.create_window(100, 0, window=entry, anchor="center")
	c.create_rectangle(x, y, x2, y2, fill='gray')
	c.create_text(x+100, y+20, text=text, font="Calibri 15", anchor=tk.W)
	descripti = '\n'.join(wrap_text(description, 440, text_font))
	c.create_text(x+100, y+40, text=descripti, font="Calibri 13", anchor=tk.NW)

	if img_url not in images_dict:
		img_data = requests.get(img_url, headers=headers).content
		img_file = io.BytesIO(img_data)
		image1 = Image.open(img_file)
		image1 = image1.resize((90, 90), Image.BICUBIC)
		images_dict[img_url] = ImageTk.PhotoImage(image1)

	image = images_dict[img_url]
	click=c.create_image(70, y+55, anchor=tk.CENTER, image=image)

	c.tag_bind(click, '<Button-1>', lambda event, url=img_url: image_click(event, url))

def image_click(event, img_url):
	c.delete("all")
	for i in range(len(mods)):
		if mods[i][2]==img_url:
			mod0=i
			break
	html = get_mods(f'https://modrinth.com/mod/{mods[mod0][3]}/versions')
	parse_versions(html)

def parse_versions(html):
	global versions
	versions=True
	version_title = []
	c.yview_moveto(c.yview()[0])
	soup = BeautifulSoup(html, 'html.parser')
	version_cards = soup.find_all('div', class_='featured-version button-transparent')
	for version_card in version_cards:
		version_title_element = version_card.find('a', class_='top')
		version_game = version_card.find('div', class_='game-version item').text
		if version_title_element is not None:
			version_title.append((version_title_element.text, 'https://modrinth.com'+version_title_element.get('href'), version_game))
	i = 0
	rectangles = []
	while not len(version_title) == int(i):
		rect = c.create_rectangle(20, i*80, 480, i*80+50, fill='gray')
		c.create_text(35, i*80+15, text=f'{version_title[i][2]} || {version_title[i][0]}', font="Calibri 15", anchor=tk.NW)
		rectangles.append(rect)
		i += 1
	for rect_index, rect in enumerate(rectangles):
		c.tag_bind(rect, '<Button-1>', lambda event, mod_ver=version_title[int(i)-1][1]: ver_download(event, mod_ver))

def ver_download(event, ver):
	html=get_mods(ver)
	download(html)
	back(0)

def download(html):
	soup = BeautifulSoup(html, 'html.parser')
	download_button = soup.find('div', class_='file primary')
	response=requests.get(download_button.find('a').get('href'))
	with open(f'{download_button.text[:str(download_button.text).find(".jar")]}.jar', 'wb') as file:
		file.write(response.content)

def scroll(event):
	if event.delta > 0:
		c.yview_scroll(-1, "units")
	else:
		c.yview_scroll(1, "units")

def back(event):
	global versions
	if versions is True:
		versions=False
		c.delete('all')
		c.yview_moveto(c.yview()[0])
		parse_html(get_mods('https://modrinth.com/mods'))

def next_page(event):
	global page, versions
	page=page+1
	versions=True
	back(0)

def back_page(event):
	global page, versions
	if page>0:
		page=page-1
		versions=True
		back(0)

def search(event):
	global search_word, versions
	if not entry.get() is None:
		search_word=entry.get()
		versions=True
		back(0)

window = tk.Tk()
c = tk.Canvas(window, height=500, width=500)
c.pack()

entry = tk.Entry(window)

text_font = Font(family="Calibri", size=15)

window.bind_all("<MouseWheel>", scroll)
window.bind("<Escape>", back)
window.bind("<Right>", next_page)
window.bind("<Left>", back_page)
window.bind("<Return>", search)

parse_html(get_mods('https://modrinth.com/mods'))

window.mainloop()
