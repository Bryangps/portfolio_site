from zboxcrossvendasbebidas import app
from flask import redirect, request, render_template, flash, url_for
from zboxcrossvendasbebidas.forms import FormLogin, FormCriarCadastro
from zboxcrossvendasbebidas.models import Usuario

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        flash('Login feito com sucesso', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login)


@app.route('/criar_conta', methods=['GET', 'POST'])
def criar_cadastro():
    form_criarcadastro = FormCriarCadastro()
    if form_criarcadastro.validate_on_submit():
        cry_senha =
        usuario = Usuario(username=form_criarcadastro.username.data, email=form_criarcadastro.email.data, senha=)
        flash('Conta criada com sucesso', 'alert-success')
        return redirect(url_for('home'))
    return render_template('criarCadastro.html', form_criarcadastro=form_criarcadastro)


@app.route('/cadastra/bebidas')
def cadastra_bebidas():
    return 'home'


@app.route('/sair')
def sair():
    return 'home'
