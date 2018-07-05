from bs4 import BeautifulSoup
import requests
import os

#enter URL
url = "http://www.cricbuzz.com/cricket-match/live-scores"

req = requests.get(url)

data = req.text
soup = BeautifulSoup(data,'html.parser')
#using beautifulsoup for scraping

file = open("ci.txt","a")


for score in soup.findAll("div",{"class":"cb-lv-scrs-col"}):
	#print score.text	
	scre = score.text
#scre in unicode form
	scree = scre.encode('utf-8')
#encode it to convert in string form 
	#ss = os.path.split(s)
	#print(type(s))
	print scree
	print '\n'
	file.write(scree)

file.close()

	#scoreIT = score.findAll('span')
	#for scre in scoreIT:
	#	print scre.text
	

#score = soup.findAll("div",{"class":"cb-lv-scrs-col"})
#print score.text	
#scre = score.text
#scree = scre.encode('utf-8')
#s = str(scree)
#ss = os.path.split(s)
#print(type(s))
#print ss	
#print '\n'
#file.write(ss)

#file.close()	

	#else:
	#	print "hello"

print "completed"
