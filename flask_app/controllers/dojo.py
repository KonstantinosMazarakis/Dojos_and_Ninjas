from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojos import Dojo
from flask_app.models.ninjas import Ninja

# nothing on the page
@app.route("/")
def index():
    return redirect ("/dojos")

#--------------------------------------------------------

    # all dojos
@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", dojos = dojos)


    #POST form from new user ^
@app.route("/dojos/new_dojo_post", methods=["POST"])
def new_dojo_post():
    new_dojo = request.form
    Dojo.add_dojo(new_dojo)
    return redirect("/dojos")

#--------------------------------------------------------

@app.route("/dojos/<int:id>")
def dojos_ninja(id):
    ninjas = Ninja.dojos_ninja({'id':id})
    dojo = Dojo.get_one_dojo({'id': id})
    return render_template("dojosninja.html", ninjas = ninjas, dojo = dojo)

#--------------------------------------------------------

@app.route("/dojos/new_ninja")
def new_ninja():
    dojos = Dojo.get_all()
    return render_template("ninjas.html" , dojos = dojos)

@app.route("/dojos/new_ninja_post", methods=["POST"])
def new_ninja_post():
    new_ninja = request.form
    Ninja.add_ninja(new_ninja)
    return redirect("/dojos")