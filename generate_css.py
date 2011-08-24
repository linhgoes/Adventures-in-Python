import csv
codereader = csv.reader(open('country-codes.txt', 'r'), delimiter="\t")
waterreader = csv.reader(open('water-source1.txt', 'r'), delimiter="\t")

alpha3to2 = {}
i = 0
next(codereader)
for row in codereader:
	alpha3to2[row[1]]=row[0]
	
i = 0
next(waterreader)
for row in waterreader:

	if row[1] in alpha3to2 and row[6]:
		alpha2 = alpha3to2[row[1]].lower()
		pct = int(row[6])
		if pct == 100:
			fill = "#0868AC"
		elif pct > 90:
			fill = "#43A2CA"
		elif pct > 80:
			fill = "#7BCC4"
		elif pct > 70:
			fill = "#BAE4BC"
		elif pct > 60:
			fill = "#F0F9E8"

		else:
			fill = "#CCCCCC"
		print '.' + alpha2 + ' { fill: ' + fill + '}'

	i += 1