#Desarrollada con: https://v0.app/ INGRESA bolakos@gmail.com
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mi-hospital')
def mi_hospital():
    return render_template('mi_hospital.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/ing-sistemas')
def ing_sistemas():
    return render_template('ing_sistemas.html')

@app.route('/teleconsulta')
def teleconsulta():
    return render_template('teleconsulta.html')

@app.route('/profesional')
def profesional():
    return render_template('profesional.html')

@app.route('/mi-agenda')
def mi_agenda():
    return render_template('mi_agenda.html')

@app.route('/go')
def ginecologia_obstetricia():
    return render_template('go.html')

@app.route('/videolap')
def videolap():
    return render_template('videolap.html')

@app.route('/salud-tic')
def salud_tic():
    return render_template('salud_tic.html')

@app.route('/destacado')
def destacado():
    return render_template('destacado.html')

if __name__ == '__main__':
    app.run(debug=True)
