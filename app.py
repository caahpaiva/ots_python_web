from flask import Flask, render_template, request, session, flash, redirect, url_for

app = Flask("Meu App")
app.config['SECRET_KEY'] = 'pudim'

posts = [
    {
        "titulo": "Minha primeira postagem",
        "texto": "teste"
    },
    {
        "titulo": "Segundo Post",
        'texto': "outro teste"
    }
]

@app.route('/')
def exibir_entradas():
    entradas = posts # Mock das postagens
    return render_template('exibir_entradas.html', entradas=entradas)


@app.route('/layout')
def layout():
    return render_template('layout.html')

@app.route('/outro')
def outro():
    return render_template('outro_template.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    erro = None
    if request.method == "POST":
        if request.form['username']  == "admin" and request.form['password'] == "admin":
            session['logado'] = True
            flash("Login efetuado com sucesso!")
            return render_template('exibir_entradas.html')
        erro = "Usuário ou senha inválidos"        
    return render_template('login.html', erro=erro)