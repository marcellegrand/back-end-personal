#Importamos render_template para renderizar plantillas de jinja2
from flask import render_template
#
from . import admin

@admin.route('/login')
def login():
    return render_template('login.html')