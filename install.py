# this file should be run to create all the required databases and initialise the setting.

import mysql.connector as sql

print("Initializing the sql database connection.......")
# creating connection 
con = sql.connect(host = "localhost", user = "root", passwd = "")
if con.is_connected():
    print("sql database connected!!........")
# creating the cursor object
cursor = con.cursor()

# asks the user for the database name
db_name = input("What name would you like to keep for the database? ")

# this creates the database for the user
cursor.execute("create database if not exists "+db_name)
cursor.execute("use "+db_name)



# this creates the basic user table
cursor.execute("create table user (uno int not null primary key, uid varchar(20) not null unique, u_pwd varchar(20) not null)")
cursor.execute("insert into user values(0,'admin', 'admin')")

# this creates the subjects table
cursor.execute("create table sub (s_id int not null primary key, u_id json, s_name varchar(20))")
cursor.execute("insert into sub values(0,'[0]','null')")

# this creates the chapter table
cursor.execute("create table chp (c_id int primary key, c_name varchar(20) not null, s_name varchar(20), uno json)")
cursor.execute("insert into chp values(0, 'null',0)")

# this creates the tag table
cursor.execute("create table tag (c_id int primary key, tag json)")


print("Tables and database succesfully created and initialised!!!")