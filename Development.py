import csv
codereader = csv.reader(open('country-codes.txt', 'r'), delimiter="\t")
devreader = csv.reader(open('development_code.csv', 'rU'), delimiter=",")

alpha3to2 = {}
i = 0
next(codereader)
for row in codereader:
	alpha3to2[row[1]]=row[0]

i = 0
next(devreader)
for row in devreader:

	if row[1] in alpha3to2 and row[2]:
		alpha2 = alpha3to2[row[1]].lower()
		pct = int(row[2])
		if pct == 5:
			fill = "#0868AC"
		elif pct == 4:
			fill = "#43A2CA"
		elif pct == 3:
			fill = "#7BCC4"
		elif pct == 2:
			fill = "#BAE4BC"
		elif pct == 1:
			fill = "#F0F9E8"
		
		else:
			fill = "#CCCCCC"
		print '.' + alpha2 + ' { fill: ' + fill + '}'
	
	i += 1