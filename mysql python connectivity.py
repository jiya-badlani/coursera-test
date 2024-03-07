import mysql.connector
db=mysql.connector.connect(host="localhost",
                           user="root",
                           password="root",
                           database="hospital2")
cur=db.cursor()

def use_database():
    cur.execute("use hospital2")
    db.commit()

def create_table_doc():
    cur.execute("create table doctors(id int primary key, \
                                      name varchar(100), \
                                      dept varchar(50), \
                                      sex varchar(1), \
                                      experience int, \
                                      consultaion_fee int)")
    db.commit()

try:
    create_table_doc()
except:
    print("table doctors exists")

def insert():
    try:
        it='yes'
        while it=='yes':
            di=int(input("Enter id: "))
            dn=input("Enter name: ")
            dd=input("Enter department: ")
            ds=input("Enter sex: ")
            de=int(input("Enter experience: "))
            df=int(input("Enter consultation fee: "))
            query="insert into doctors values({},'{}','{}','{}',{},{}) \
                  ".format(di,dn,dd,ds,de,df)
            cur.execute(query)
            db.commit()
            it=input("Do you want to continue? (yes/no) ")
    except:
        it=input("An error occured.")

def delete():
    try:
        query="delete from doctors where consultaion_fee>300"
        cur.execute(query)
        db.commit()
    except:
        print("Error")

def increase():
    try:
        query="update doctors set consultaion_fee+=200 where experience>10"
        cur.execute(query)
        db.commit()
    except:
        print("Error")

def displayf():
    try:
        query="select * from doctors where sex='F'"
        cur.execute(query)
        db.commit()
    except:
        print("Error")
        
def display():
    query="select * from doctors"
    cur.execute(query)
    db.commit()

        
while True:
    print("~"*60)
    print("What do you want to do? \n \
          1. Insert a new record \n \
          2. delete a record with consultaion fee>300 \n \
          3. increase the consultaion fee by 200 for doctors whose experience>10\n \
          4. display records of all female employees \n \
          5. display all records \n \
          0. Exit")
 
    a=int(input("Please enter a number from 1-5: "))
    if a==1:
        insert()
    if a==2:
        delete()
    if a==3:
        increase()
    if a==4:
        displayf()
    if a==5:
        display()
    if a==0:
        print("Thank you.")
        break
