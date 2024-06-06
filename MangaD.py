import requests
from io import BytesIO

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

url=input('URL(num.jpg): ')
n=input('len of manga: ')

for i in range(int(n)+1):
	response=requests.get(url.replace('num', str(i)), headers=headers)
	image_data=BytesIO(response.content)

	with open(f'{i}.jpg', 'wb') as f:
		f.write(image_data.getvalue())