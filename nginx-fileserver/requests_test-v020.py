import requests

url = 'http://google.com/favicon.ico'
url2 = 'https://cloud.io-jupiter.de//index.php/s/DM8wqe9NW8TAT2e?path=%2F&openfile=398202'

r = requests.get(url2, allow_redirects=True)
# open('google.ico', 'wb').write(r.content)
open('testfile.txt', 'wb').write(r.content)

# THIS IS VERSION 0.2.0