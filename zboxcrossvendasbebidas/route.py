from zboxcrossvendasbebidas import app, database, bcrypt
from flask import redirect, request, render_template, flash, url_for
from zboxcrossvendasbebidas.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
@login_required
def index():
    return redirect(url_for('login'))


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    # Cadastro Do Usuário
    if request.method == 'POST' and 'submit-registration' in request.form:
        nome = request.form['name']
        email = request.form['email-registration']
        senha = request.form['password-registration']
        senha_cript = bcrypt.generate_password_hash(senha)
        usuario = Usuario(username=nome, email=email, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash('Login feito com sucesso', 'alert-success')
        return redirect('home')
    return render_template('login.html')


# @app.route('/criar_conta', methods=['GET', 'POST'])
# def criar_cadastro():
#     if request.method == 'POST' and 'submit-registration' in request.form:
#         nome = request.form['nome']
#         email = request.form['email-registration']
#
#         print(nome)
#         print(email)
#         return redirect('home')
#     return render_template('criarCadastro.html')
#
#     # form_criarcadastro = FormCriarCadastro()
#     # if form_criarcadastro.validate_on_submit():
#     #     senha_cript = bcrypt.generate_password_hash(form_criarcadastro.senha.data)
#     #     usuario = Usuario(username=form_criarcadastro.username.data, email=form_criarcadastro.email.data, senha=senha_cript)
#     #     database.session.add(usuario)
#     #     database.session.commit()
#     #     flash('Conta criada com sucesso', 'alert-success')
#     #     return redirect(url_for('home'))



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

