from flask import Flask, render_template, request, redirect
app = Flask(__name__)

class cadInfDigital:
    def __init__(self, nome, plataforma, seguidores, interesse):
        self.nome = nome
        self.plataforma = plataforma
        self.seguidores = seguidores
        self.interesse = interesse

lista = []


@app.route('/influenciadores')
def infDigital():
    return render_template('InfDigital.html', Titulo ="Influenciadores Digitais: ", ListaInfDigital = lista)


@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo = "Cadastro de Influenciadores")


@app.route('/criar', methods= ['POST'])
def criar():
    nome = request.form['nome']
    plataforma = request.form['plataforma']
    seguidores = request.form['seguidores']
    interesse = request.form['interesse']

    obj = cadInfDigital(nome, plataforma, seguidores, interesse)
    lista.append(obj)
    return redirect('/influenciadores')



if __name__ == '__main__':
    app.run()
