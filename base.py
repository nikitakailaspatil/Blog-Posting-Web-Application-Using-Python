from flask import *
from db_module import *
app=Flask(__name__)
@app.route("/")#main page
def main_page():
    return render_template("mainpage.html") 
    
@app.route("/a_register_page") #register for author
def author_reg():
    return render_template("author_reg.html")

@app.route("/a_reg" , methods=["post"])#connect to database for author
def db_a_reg():
    a_username=request.form["a_username"]
    a_password=request.form["a_password"]
    a_city=request.form["a_city"]
    t=(a_username,a_password,a_city)
    insert_author(t)
    return render_template("display_author_acc.html")
@app.route("/a_login")
def a_login(): #author login page
    return render_template("a_login_page.html")

@app.route("/author_login",methods=["post"])
def author_db_login():#author login page connect to db
        username = request.form['a_username']
        password = request.form['a_password']
        t=(username,password)
        data=author_login(t)
        for i in data:
            return render_template("display_author_acc.html",user=username)
        else:
            return redirect("/a_register_page")

@app.route("/add_post")#author add post
def a_post():
    return render_template("add_post_author.html")
@app.route("/post_add",methods=["post"])#connect to db of post
def author_post():
    p_uname=request.form['a_post_name']
    p_title=request.form["a_title"]
    p_blog=request.form["blog_a"]
    t=(p_uname,p_title,p_blog)
    post_author(t)
    return redirect("/")

@app.route("/view_post/<user>")
def a_view(user):
    data=view_post_author(user)
    return render_template("author_post_view.html",res=data)
    

@app.route("/u_register_page")#register for user
def user_reg():
    return render_template("user_reg.html")

@app.route("/u_reg" , methods=["post"])#connect to database for user
def db_u_reg():
    u_username=request.form["u_username"]
    u_password=request.form["u_password"]
    u_city=request.form["u_city"]
    t=(u_username,u_password,u_city)
    insert_user(t)
    return redirect("/")


@app.route("/u_login")#login as user
def user_login():
    return render_template("user_loginpage.html")
@app.route("/user_login",methods=['post']) #connect db for login as user
def u_login_db_page():
    u_name=request.form["u_uname"]
    u_password=request.form["u_password"]
    t=(u_name,u_password)
    data=user_login_db(t)
    for t in data:
        data=view_all_post_user()
        return render_template("all_post_view_user.html",res=data)
    else:
        return redirect("/u_register_page")
if (__name__=="__main__"):
    app.run(debug=True)