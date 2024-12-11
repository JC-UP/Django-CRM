# Install Mysql on computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = '127.0.0.1',
	user = 'root',
	passwd = 'lemeeSLIP!143'

	)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE readingfantasy")

print ("All Done!")
