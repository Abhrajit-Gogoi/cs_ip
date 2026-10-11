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

# defining lists to use in the future
u_name=[]
s_list=[]
cursor.execute("select uno from user order by uno desc limit 1;")
uno = cursor.fetchall()[0][0] + 1
login = "F"
current_sid = 0




# creating list of username
def username():
    cursor.execute("select uid from user")
    s = cursor.fetchall()
    for i in range(0,len(s)):
        u_name.append(s[i][0])


# creating list of subjects
def slist():
    cursor.execute("select s_name from sub;")
    s = cursor.fetchall()
    for i in range(0,len(s)):
        s_list.append(s[i][0])



#create user function
def c_user():
    uno=0
    uid=''
    uid = input("Enter username: ").strip()
    username()
    if uid in u_name:
        print("Username already taken")
        return 
    pwd = input("Enter password: ").strip()
    cursor.execute("insert into user values ("+str(uno)+",\'"+uid+"\',\'"+pwd+"\');")
    print("user succesfully registered!!")




# login function
def login():
    uid=''
    pwd=''
    uid = input("Enter your username: ").strip()
    username() # updates username list and checks
    if uid not in u_name:
        print("Invalid username....")
        return False
    cursor.execute("select u_pwd from user where uid=\'"+uid+"\'")
    pwd = input("enter password: ").strip()
    if pwd != cursor.fetchall()[0][0]:
        print("invalid password")
        return False
    print("Welcome " + uid+ " hope you enjoy using our services!!")
    cursor.execute("select uno from user where uid=\'"+uid+"\';")
    uno = cursor.fetchall()[0][0]
    return uno




# create subject function
def c_sub():
    cursor.execute("select s_id from sub order by s_id desc limit 1;")
    s_id = cursor.fetchall()[0][0] + 1
    slist() # updates subject list every time to check
    s_name = input("Enter subject name: ")
    if s_name in s_list:
        cursor.execute("select u_id from sub where s_name='"+s_name+"\'")
        uida = eval(cursor.fetchall()[0][0])
        uida.append(uno)
        cursor.execute("update sub set u_id='"+str(uida)+"' where s_name=\'"+s_name+"\'")
        print("Successfully created!!")
    else:
        cursor.execute("insert into sub values("+str(s_id)+",'["+str(uno)+"]', '"+s_name+"') ")
        print("New subject successfully created!!")
        







# view subjects function
def v_sub():
    cursor.execute("select s_name from sub;")
    s=cursor.fetchall()
    r=[]
    for i in range(0,len(s)):
        r.append(s[i][0])
    print(r)
    









# ******************* MAIN *****************************

while True:
    # starting the main execution loop of the program
    print()
    print("============================ WELCOME TO MY CS-IP ====================================\n")
    if login != "T":
        print("What would you like to do? \n" \
        "\t1. Create an account. \n" \
        "\t2. Login to your account. \n" \
        "\t3. EXIT.")
        ch = int(input("Enter the number corresponding to your choice: "))
        if ch ==1:
            c_user()
            continue
        
        elif ch ==2:
            l = login()
            if l != False:
                uno = l
                login = "T"
            else:
                continue 
        elif ch == 3:
            print("Bye Byeeeeee")
            break
        else:
            print("Invalid situation")
            continue
    elif login == "T":
        print("What would you like to do?")
        print("1. View subjects \n2. Select subjects \n3. Exit")
        ch = int(input("Enter the number corresponding to your choice: "))
        if ch
    
    







# committing the changes
con.commit()

# closing the cursor and the connection
cursor.close()
con.close()


