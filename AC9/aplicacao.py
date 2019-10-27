from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def ola():
    return '<h1>Aula Flask</h1>'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/detalhes')
def detalhes():
    return render_template("detalhes.html")

@app.route('/disciplinas')
def disciplinas():
    return render_template("disciplinas.html")
    
@app.route('/listadecursos')
def listadecursos():
    return render_template("listadecursos.html")

@app.route('/notícias')
def notícias():
    return render_template("notícias.html")
app.run()