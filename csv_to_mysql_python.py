import csv
import MySQLdb

#establish connection to the database
mydb = MySQLdb.connect(host='igor.gold.ac.uk',
    user='<username>',
    passwd='<pass>',
    db='<database_name')
cursor = mydb.cursor()

# read csv file
csv_data = csv.reader(file('<csv_file>'))
for row in csv_data:
    # importing to MySQL database
    cursor.execute('INSERT INTO bitscrape VALUES(%s, %s, <times_number_of_columns>)', row)

#close the connection to the database
mydb.commit()
cursor.close()
print "Done"
