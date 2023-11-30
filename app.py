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

@app.route('/excluir/<nomeinf>', methods=['GET','DELETE'])
def excluir(nomeinf) :
    for i, inf in enumerate(lista):
        if inf.nome == nomeinf:
            lista.pop(i)
            break
    return redirect('/influenciadores')

@app.route('/editar/<nomeinf>', methods=['GET'])
def editar(nomeinf):
    for i, inf in enumerate(lista):
        if inf.nome == nomeinf:
            return render_template("Editar.html", influenciadores=inf, Titulo="Alterar Influenciador")

@app.route('/alterar', methods = ['POST','PUT'])
def alterar():
    nome = request.form['nome']
    for i, inf in enumerate(lista):
        if inf.nome == nome:
            inf.nome = request.form['nome']
            inf.plataforma = request.form['plataforma']
            inf.seguidores = request.form['seguidores']
            inf.interesse = request.form['interesse']
    return redirect('/influenciadores')



if __name__ == '__main__':
    app.run()
