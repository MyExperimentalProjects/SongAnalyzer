import requests
from bs4 import BeautifulSoup,SoupStrainer
from urllib import FancyURLopener
import json
class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
openurl = MyOpener().open

base_url = "http://www.metrolyrics.com"

res = requests.get("http://www.metrolyrics.com/roger-waters-lyrics.html",headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'});
soup = BeautifulSoup(res.text,'html.parser')
listOfLyrics = soup.find('table',attrs={'class':'songs-table compact'})

lyricsList = []
testfile = open('rogerwater.txt', 'w')
songsfile = open('songs.txt', 'w')
for details in listOfLyrics.find_all('a',href=True):
	if '-roger-waters.html' not in details['href']:
		continue;
	songsfile.write(details['href'])
	songsfile.write("\n")

  	lyricsInfo = {}
  	lyricURL = details['href']
  	
  	lyricHTML = BeautifulSoup(openurl(details['href']).read(),'html.parser',parse_only=SoupStrainer('div',{'id':'lyrics-body-text'}))
  	#divToParse = lyricHTML.find('div',{'class':'lyrics-body-text'})
  	#lyricSoup = divToParse.find_all('div')[5]
  	dodgyLyrics = lyricHTML.text.strip().split('\n')

#for i in dodgyLyrics:
#    if '{' in i:
#      dodgyLyrics.remove(i)

	properLyrics = '\n'.join(dodgyLyrics)

	lyricsInfo['url'] = lyricURL
	lyricsInfo['lyrics'] = properLyrics
	testfile.write(properLyrics)

	testfile.write("\n====================\n")
	testfile.write(lyricURL);
	testfile.write("\n==========xxxxx==========\n")
	lyricsList.append(lyricsInfo)
  
with open('rogerwaterlyrics.json', 'w') as outfile:
	json.dump(lyricsList,outfile,sort_keys = True, indent = 4)
