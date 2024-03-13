from zboxcrossvendasbebidas import app
from flask import redirect, request, render_template
from zboxcrossvendasbebidas.forms import FormLogin, FormCriarCadastro


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    form_login = FormLogin()

    return render_template('login.html', form_login=form_login)


@app.route('/criar_conta')
def criar_cadastro():
    form_criarcadastro = FormCriarCadastro()
    return render_template('criarCadastro.html', form_criarcadastro=form_criarcadastro)


@app.route('/cadastra/bebidas')
def cadastra_bebidas():
    return 'home'


@app.route('/sair')
def sair():
    return 'home'
