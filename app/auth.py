from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import get_user_by_username, add_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = get_user_by_username(username)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('views.dashboard'))
        else:
            flash('Login failed. Check your username and/or password.')
    return render_template('login.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if current_user.role != 'admin':
        flash('Only administrators can register new users.')
        return redirect(url_for('views.home'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')

        if get_user_by_username(username):
            flash('Username already exists.')
            return redirect(url_for('auth.register'))
        
        hashed_password = generate_password_hash(password, method='sha256')
        add_user(username, hashed_password, role)
        flash('User registered successfully.')
        return redirect(url_for('auth.login'))
    return render_template('register.html')