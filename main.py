# importing the connector package
import mysql.connector as sql


# LEGEND:
# uno : user number
# uid : user id
# u_pwd : user password


# ****************************** COOL INITIALIZATION SETUP *********************************

print("Initializing the sql database connection.......")
# creating connection 
con = sql.connect(host = "localhost", user = "root", passwd = "", database ="cs_ip")
if con.is_connected():
    print("sql database connected!!........")
# creating the cursor object
cursor = con.cursor()

# ******************************************************************************************

cursor.execute("select * from user;")
cursor.fetchall()



cursor.execute("select uno from user order by uno desc limit 1;")
def c_user():
    cursor.execute("select uno from user order by uno desc limit 1")



# fetch part
print(cursor.fetchall()[0][0] + 1)


# committing the changes
con.commit()

# closing the cursor and the connection
cursor.close()
con.close()