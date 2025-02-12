#store standard routes for the website
#non authenication routes

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import  login_required, current_user
views = Blueprint('views', __name__)

#main login for users
@views.route('/', methods=['GET', 'POST'])
@login_required 
def home():
    return render_template("home.html", user=current_user)

# #admin login
# @views.route('/admin/', methods=['GET', 'POST'])
# # @login_required
# def adminIndex():
#     return render_template("admin/index.html", title="Admin Login", user=current_user)

# #user login
# @views.route('/user/', methods=['GET', 'POST'])
# # @login_required
# def userIndex():
#     return render_template("user/index.html", title="User Login", user=current_user)
