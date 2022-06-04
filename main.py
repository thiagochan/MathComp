from flask import Flask, render_template, request
import sqlite3 

banco = sqlite3.connect('database.db', check_same_thread=False)
db = banco.cursor()

app = Flask(__name__)

#
@app.route('/', methods = ["GET", "POST"])
def index():
    return render_template("layout.html")

@app.route('/event', methods = ["GET", "POST"])
def event():
    #código para fazer a checagem das respostas
    if request.method == "POST": #se foi submetido um formulário
        score = 0 #zere a score
        user_answer = request.form.getlist("answers") #pegue as informações do usuário
        oa = db.execute("SELECT answer_1, answer_2, answer_3 FROM answers") #pegue as info da database

        #as info da database vem em tuple ent transformei em list
        official_answer = oa.fetchall()[0] 
        for i, j in zip(list(official_answer), user_answer): #comparei as listas usando umas funções de python
            if str(i) == str(j):
                score+=1
        print(score)
    #render_template é uma função q renderiza uma página, desse modo que eu usei independentemente do que o
    #usuário tiver feito, se foi get ou post, renderizará a página normalmente
    return render_template("event.html")
    
if __name__ == "__main__":
    app.run(debug=True)