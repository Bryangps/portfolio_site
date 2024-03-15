from zboxcrossvendasbebidas import app, database, bcrypt
from flask import redirect, request, render_template, flash, url_for
from zboxcrossvendasbebidas.forms import FormLogin, FormCriarCadastro
from zboxcrossvendasbebidas.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
@login_required
def index():
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash('Login feito com sucesso', 'alert-success')
            return redirect(url_for('home'))
        else:
            flash('Falha no login. E-mail ou Senha Incorretos', 'alert-danger')
    return render_template('login.html', form_login=form_login)


@app.route('/criar_conta', methods=['GET', 'POST'])
def criar_cadastro():
    form_criarcadastro = FormCriarCadastro()
    if form_criarcadastro.validate_on_submit():
        senha_cript = bcrypt.generate_password_hash(form_criarcadastro.senha.data)
        usuario = Usuario(username=form_criarcadastro.username.data, email=form_criarcadastro.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash('Conta criada com sucesso', 'alert-success')
        return redirect(url_for('home'))
    return render_template('criarCadastro.html', form_criarcadastro=form_criarcadastro)


@app.route('/cadastra/bebidas')
@login_required
def cadastra_bebidas():
    return 'home'


@app.route('/perfil')
@login_required
def perfil():
    return 'perfil'


@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash('Logout Feito com Sucesso', 'alert-seccess')
    return redirect(url_for('login'))

