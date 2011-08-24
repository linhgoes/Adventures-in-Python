import urllib2
from BeautifulSoup import BeautifulSoup
#Create/open a file called wunder.txt
f=open('wunder-data.txt', 'w')

#Iterate through months and day
for m in range(1, 13):
	for d in range (1, 32):
		
		#Check if already gone through month
		if (m == 2 and d > 28):
			break
		elif(m in [4,6,9,11] and d > 30):
			break
			
		#Open wundergrand.com url
		timestamp = '2010' + str(m) + str(d)
		print "Getting data for " + timestamp
		url = "http://www.wunderground.com/history/airport/KBUF/2010/" + str(m) + "/" + str(d) + "/DailyHistory.html"
		page = urllib2.urlopen(url)

		#Get temp
		soup = BeautifulSoup(page) 
		#dayTemp =soup.body.nobr.b.string
		dayTemp=soup.findAll(attrs={"class":"nobr"})[5].span.string

		#format month
		if len(str(m)) < 2:
			mStamp = '0' + str(m)
		else: 
			mStamp = str(m)

		#Format day
		if len(str(d))<2:
			dStamp = '0'+str(d)
		else:
			dStamp = str(d)

		#Build timestamp
		timestamp = '2010' + mStamp + dStamp

		#Write timestamp
		f.write(timestamp + ',' + dayTemp + '\n')

f.close
