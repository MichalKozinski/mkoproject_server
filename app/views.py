from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import add_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        menu_items = ['add_order', 'plan', 'weekly_plan', 'add_employee', 'check_order', 'production_report', 'register']
    else:
        menu_items = ['add_order', 'check_order']
    return render_template('dashboard.html', menu_items=menu_items)

@views.route('/add_order')
@login_required
def add_order():
    return render_template('add_order.html')

@views.route('/plan')
@login_required
def plan():
    return render_template('plan.html')

@views.route('/weekly_plan')
@login_required
def weekly_plan():
    return render_template('weekly_plan.html')

@views.route('/add_employee', methods=['GET', 'POST'])
@login_required
def add_employee():
    if current_user.role != 'admin':
        flash('Only admins can add employees.')
        return redirect(url_for('views.dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        add_user(username, password, role)
        flash('Employee added successfully.')
        return redirect(url_for('views.dashboard'))
    return render_template('add_employee.html')

@views.route('/check_order')
@login_required
def check_order():
    return render_template('check_order.html')

@views.route('/production_report')
@login_required
def production_report():
    return render_template('production_report.html')