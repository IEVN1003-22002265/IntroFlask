from flask import Flask, render_template, request
import math


 
 
app=Flask(__name__)

 
@app.route("/") #decorador o ruta
def index():
    titulo="pagina de inicio"
    listado = ['Python','Jinja2','HTML', 'CSS']
    return render_template("index.html",titulo=titulo, listado=listado)

@app.route("/operabas", methods= ("GET","POST"))
def operasbas():
    n1=0
    n2=0
    res=0
    operacion=''
    if request.method=="POST":
        n1=request.form.get('n1')
        n2=request.form.get('n2')
        if request.form.get('operacion')=='sumar':
            res=float(n1)+float(n2)
        if request.form.get('operacion')=='restar':
            res2=float(n1)-float(n2)
        if request.form.get('operacion')=='multiplicar':
            res3=float(n1)*float(n2)

    return render_template('operabas.html', n1=n1, n2=n2, res=res)

@app.route("/distancia", methods=("GET", "POST"))
def distancia():
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    res = 0

    if request.method == "POST":
        x1 = request.form.get('x1')
        y1 = request.form.get('y1')
        x2 = request.form.get('x2')
        y2 = request.form.get('y2')

        dx = float(x2) - float(x1)
        dy = float(y2) - float(y1)

        total = (dx * dx) + (dy * dy)
        res = math.sqrt(total)

    return render_template('distancia.html', x1=x1, y1=y1, x2=x2, y2=y2, res=res)

@app.route("/hola")
def hola():
    return "<h1> Hola PWA - IEVN1003</h1>"
 
 
@app.route("/user/<string:nom>")
def user(nom):
    return "<h1>Hola User: {} </h1>".format(nom)
 
@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return "ID: {} nombre: {}".format(id,username)
 
@app.route("/suma/<float:n1>/<float:n2>")
def func(n1, n2):
    return "la suma es: {}".format(n1+n2)
 
 
if __name__=="__main__":
    app.run(debug=True)