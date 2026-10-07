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


#create user function

def c_user():
    uno=0
    uid=''
    cursor.execute("select uno from user order by uno desc limit 1;")
    uno = cursor.fetchall()[0][0] + 1
    print(uno)
    cursor.execute("select uid from user")
    u_name = cursor.fetchall()[0]
    uid = input("Enter username: ").strip()
    if uid in u_name:
        print("Username already taken")
        return 
    pwd = input("Enter password: ").strip()
    cursor.execute("insert into user values ("+str(uno)+",\'"+uid+"\',\'"+pwd+"\')")
    print("user succesfully registered!!")


# ******************* MAIN *****************************
c_user()



# committing the changes
con.commit()

# closing the cursor and the connection
cursor.close()
con.close()


