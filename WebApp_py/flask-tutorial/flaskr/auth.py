import functools 

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db 

bp = Blueprint(
    name='auth', # this becomes an identifier for redirection
    import_name=__name__, 
    url_prefix='/auth'
)

# this decoratator associates the URL /register 
# with the register() view function
# when a request is sent to /auth/register
# it passes the request into the register
# view() function, you may also refer to it as 
# the 'register' view for handling which will 
# then return a response
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.' 
        elif not password:
            error = 'Password is required.'
        
        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered"
            else:
                return redirect(url_for("auth.login")) # this redirects to the URL associated with the login view based on its name. Note that the 'auth' there refers not to the script name but the blueprint's name 
        
        # flashes a mesage to the next request
        flash(error)

    return render_template('auth/register.html')

@bp.route('/view', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None 
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            # session is a dictionary that stores
            # data across requessts
            # when validation succeeds, the user
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        
        flash(error)

    return render_template('auth/login.html')

# this decorator marks a function to be 
# run before the view functions associated with the 
# blueprint 
@bp.before_app_request
def load_logged_in_user():
    # using the user_id we obtained from the login view
    # we place the user_id into the user attribute in 
    # g *which lasts for the length of the request*
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None 
    else: 
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view