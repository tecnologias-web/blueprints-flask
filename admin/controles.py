from admin import admin_bp
from admin import admin_bp
from flask import render_template


@admin_bp.route('/')
def admin():
    return render_template('admin.html')