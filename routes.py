from app import app
from flask import render_template, redirect, url_for

@app.route('/')  # Что будет, если зайти на главную страницу сайта
def index():
    context = {'title': 'My first site'}  # Набор элементов, передаваемый в шаблон сайта
    return render_template('index.html', context=context)  # При переходе на главную страницу, показать шаблон index.html


@app.route('/contacts')
def contacts():
    context = {'title': 'Contacts page'}  # Набор элементов, передаваемый в шаблон сайта
    return render_template('contacts.html', context=context)