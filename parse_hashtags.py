import re
import MySQLdb

# connects to database 
mydb = MySQLdb.connect(host='igor.gold.ac.uk',
    user='*******',
    passwd='*******',
    db='*******')
cursor = mydb.cursor()

# queries the database for a column 
getdata = 'SELECT text FROM bitscrape'
cursor.execute(getdata)
results = cursor.fetchall()

# writes into an empty csv file
csv_data = open('<yourcsv','w')

# loops tweets in a column and saves them into a csv file 
for i in results: 
	for j in re.findall(r"\#\w+", i[0]):
		csv_data.write(j+' ')
	csv_data.write('\n')
csv_data.close()

print "Done"
