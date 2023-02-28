import pymysql as p
def create_con():
    con=p.connect(user="root",password="Neha@123",host="localhost",database="flask2")
    return con
def insert_author(t):
    con=create_con()
    cur=con.cursor()
    q='insert into author(username,password,city) values(%s,%s,%s)'
    cur.execute(q,t)
    con.commit()
    con.close()
    
def insert_user(t):
    con=create_con()
    cur=con.cursor()
    q='insert into user(username,password,city) values(%s,%s,%s)'
    cur.execute(q,t)
    con.commit()
    con.close()

def author_login(t):
    con=create_con()
    cur=con.cursor()
    q='select * from author where username = %s AND password = %s'
    cur.execute(q,t)
    author = cur.fetchall()
    return author

def user_login_db(t):
    con=create_con()
    cur=con.cursor()
    q='select * from user where username =%s and password =%s'
    cur.execute(q,t)
    user=cur.fetchall()
    return user

def post_author(t):
    con=create_con()
    cur=con.cursor()
    q='insert into author_post(P_UNAME , P_title , P_Post) values(%s,%s,%s)'
    cur.execute(q,t)
    con.commit()
    con.close()

def view_post_author(username):
    con=create_con()
    cur=con.cursor()
    q='select P_UNAME , P_title , P_Post from author_post where P_UNAME =%s'
    cur.execute(q,username)
    data=cur.fetchall()
    return data

def view_all_post_user():
    con=create_con()
    cur=con.cursor()
    q='select * from author_post'
    cur.execute(q)
    data=cur.fetchall()
    return data 
