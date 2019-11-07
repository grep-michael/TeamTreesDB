import requests,time,hashlib,string
import db
from bs4 import BeautifulSoup

#create a datebase class for the db file donators
database = db.database('donators.db')
#set constants
printable = set(string.printable)
s = requests.Session()
headers = {"User-Agent":"A bot for documenting all team tree donators"}

while 1:
	#get html from webpage
	content = s.get('https://teamtrees.org/',headers=headers)
	print("Request")
	#set up soup element and parse it for information
	soup = BeautifulSoup(content.content,'html.parser')
	recentPanel = soup.find(id="recent-donations")
	divs = recentPanel.findAll('div',{'class':'media pt-3'})
	print("	looping")
	for div in divs:
		name = div.find('strong').text
		message = div.find('span',{"class":"d-block medium mb-0"}).text
		ammount = div.find("span",{"class":"feed-tree-count"}).text
		date = div.find("span",{"class":"feed-datetime"}).text
		try:
			#to ensure no duplicates we take a string thats a combination
			#of all the values and hash it
			id = (name+message+ammount+date)
			id = filter(lambda x: x in printable, id) #remove non ascii characters from id string
			id = "".join(id) #join array of printable characters to string
			#hash id and use it as a PRIMARY KEY 
			id = hashlib.md5(id.encode())
			id = id.hexdigest()
			database.insert(name,message,ammount,date,id)
		except Exception as e:
			#Will print error, Hashlib/sqlite3 error
			print("	"+ str(e))
	print("Finished loop, sleeping")
	time.sleep(300)




