from app import app
from forms import LoginForm
from flask import render_template, redirect, url_for, request, flash


@app.route('/')  # Что будет, если зайти на главную страницу сайта
def index():
    context = {'title': 'My first site'}  # Набор элементов, передаваемый в шаблон сайта
    return render_template('index.html', context=context)  # При переходе на главную страницу, показать шаблон index.html


@app.route('/contacts', methods=['GET', 'POST'])  # Учу функцию воспринимать методы отправки формы
def contacts():
    context = {'title': 'Contacts page'}  # Набор элементов, передаваемый в шаблон сайта
    user = None
    if request.method == 'POST':  # Если нажали кнопку отправки формы
        form = request.form  # Связываю данные формы с функцией
        user = {  # Записываю данные из полей формы в словарь
            'name': form.get('name'),
            'surname': form.get('surname'),
            'phone': form.get('p_num')
        }
        return render_template('contacts.html', context=context, user=user)
    else:
        return render_template('contacts.html', context=context)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        form = request.form
        query = form.get('search_query')
        return redirect(f'https://google.com/search?q={query}')
    else:
        return render_template('search.html')


@app.route('/login', methods=['GET', 'POST']) # Когда пользователь зашел на страницу логина
def login():
    form = LoginForm()  # Создаю экземпляр формы
    if form.validate_on_submit():  # Если форма отправлена
        name = form.username.data
        remember = form.remember_me.data
        flash(f'На сайте вошел пользователь {name}, запомнить вход: {remember}')
        return redirect(url_for('index'))  # Перенаправляет на главную страницу сайт
    return render_template('login.html', title='Войти', form=form)  # Передаю форму в шаблон