# importing the connector package
import mysql.connector as sql


# *********** COOL INITIALIZATION SETUP *************

print("Initializing the sql database connection.......")

# ***************************************************


# creating connection 
con = sql.connect(host = "localhost", user = "root", passwd = "", database ="cs_ip")

if con.is_connected():
    print("sql database connected!!........")
