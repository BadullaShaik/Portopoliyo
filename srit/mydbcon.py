import sqlite3
con=sqlite3.connect("sdc.sqlite")
cur=con.cursor()
query="create table if not exists student(rollno text,name text,branch text)"
cur.execute(query)

ch=0

while ch!=3:
    ch=int(input("""
             1.INSERT
             2.DISPLAY
             3.EXIT
             Enter your choice :  """))
    if ch==1:
        rollno=input("Enter student rollno : ")
        name=input("Enter student name : ")
        branch=input("Enter student branch : ")

        cur.execute("insert into student values(?,?,?)",(rollno,name,branch))
        con.commit()
        print("ONE RECORD INSERTED")

    elif ch==2:
        cur.execute("select * from student")
        for record in cur.fetchall():
            print(record)

    """
cur.execute("insert into student values('102','badulla2','cse2')")
con.commit()
cur.execute("select * from student")
#print(cur.fetchall())
for re in cur.fetchall():
    print(re[1])
print("Done")"""
    
cur.close()
con.close()
