#script to convert old csv file to new csv file format
#Created by Daniel Baigel 9/19/19




#group specific headlines and categories and polarities and subjectivities into buckets
#i.e. the headlines bucket will have all headlines for each newssource

#each bucket will be headlines, categories, polarities, and subjectivities

#write to a new csv file flat_data_file.csv


import requests
import pandas as pd
from datetime import datetime as dt
import csv

#initialize arrays for entries to be grouped
dates = []
headlines = []
polarities = []
subjs = []
cats = []
sources = []

# index mappings in old file: 8 newssources
# 0 - date
# 1 - fox headline
# 2 - fox polarity
# 3 - fox subj
# 4 - fox cat
# 5 - nbc headline
# 6 - nbc polarity
# 7 - nbc subj
# 8 - nbc cat
# 9 - wp headline
# 10 - wp polarity
# 11 - wp subj
# 12 - wp cat
# 13 - abc headline
# 14 - abc polarity
# 15 - abc subj
# 16 - abc cat
# 17 - bb headline
# 18 - bb polarity
# 19 - bb subj
# 20 - bb cat
# 21 - bf headline
# 22 - bf polarity
# 23 - bf subj
# 24 - bf cat
# 25 - cd headline
# 26 - cd polarity
# 27 - cd subj
# 28 - cd cat
# 29 - st headline
# 30 - st polarity
# 31 - st subj
# 32 - st cat



#read in current csv file data_file.csv
with open('data_file.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			#print(f'Column names are {", ".join(row)}')  
			line_count += 1
		else:
			print("now we're on row: %d" %(line_count))
			
			#line has any data, i.e. not totally empty
			if any(row):
				#add all the dates
				if row[1] is not None:
					dates.append(row[0])
				if row[5] is not None:
					dates.append(row[0])
				if row[9] is not None:
					dates.append(row[0])
				if row[13] is not None:
					dates.append(row[0])
				if row[17] is not None:
					dates.append(row[0])
				if row[21] is not None:
					dates.append(row[0])
				if row[25] is not None:
					dates.append(row[0])
				if row[29] is not None:
					dates.append(row[0])

	        #add all the headlines and news source names

				if row[1] is not None:
					headlines.append(row[1])
					sources.append("Fox")
				if row[5] is not None:
					headlines.append(row[5])
					sources.append("NBC")
				if row[9] is not None:
					headlines.append(row[9])
					sources.append("Washington Post")
				if row[13] is not None:
					headlines.append(row[13])
					sources.append("ABC")
				if row[17] is not None:
					headlines.append(row[17])
					sources.append("Breitbart")
				if row[21] is not None:
					headlines.append(row[21])
					sources.append("Buzzfeed")
				if row[25] is not None:
					headlines.append(row[25])
					sources.append("China Daily")
				if row[29] is not None:
					headlines.append(row[29])
					sources.append("Sixth Tone")

			#add polarities

				if row[2] is not None:
					polarities.append(row[2])
				if row[6] is not None:
					polarities.append(row[6])
				if row[10] is not None:
					polarities.append(row[10])
				if row[14] is not None:
					polarities.append(row[14])
				if row[18] is not None:
					polarities.append(row[18])
				if row[22] is not None:
					polarities.append(row[22])
				if row[26] is not None:
					polarities.append(row[26])
				if row[30] is not None:
					polarities.append(row[30])

				#add subjs

				if row[3] is not None:
					subjs.append(row[3])
				if row[7] is not None:
					subjs.append(row[7])
				if row[11] is not None:
					subjs.append(row[11])
				if row[15] is not None:
					subjs.append(row[15])
				if row[19] is not None:
					subjs.append(row[19])
				if row[23] is not None:
					subjs.append(row[23])
				if row[27] is not None:
					subjs.append(row[27])
				if row[31] is not None:
					subjs.append(row[31])

				#add cats

				if row[4] is not None:
					cats.append(row[4])
				if row[8] is not None:
					cats.append(row[8])
				if row[12] is not None:
					cats.append(row[12])
				if row[16] is not None:
					cats.append(row[16])
				if row[20] is not None:
					cats.append(row[20])
				if row[24] is not None:
					cats.append(row[24])
				if row[28] is not None:
					cats.append(row[28])
				if row[32] is not None:
					cats.append(row[32])



			line_count += 1
	print(f'Processed {line_count} lines.')


with open('flat_file.csv', mode='w') as destFile:
    writer = csv.writer(destFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(0, len(dates)):
    	writer.writerow([dates[i], sources[i], headlines[i], polarities[i], subjs[i], cats[i]])
