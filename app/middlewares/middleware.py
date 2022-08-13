from app.blueprints.auth import blue_rg
from flask import request, redirect, url_for
from flask_login import current_user


class Middleware:
    
    @blue_rg.before_request
    def before_request():
        
        if current_user.is_authenticated == False and request.endpoint in ['blue_dashboard.dashboard']:
            return redirect(url_for('rg.loggin'))
        if current_user.is_authenticated == True and request.endpoint in ['rg.register', 'rg.loggin']:
            return redirect(url_for('home.home'))

rld_before_request = Middleware()
