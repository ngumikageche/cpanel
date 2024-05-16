# app.py

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect  # Import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask import jsonify


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    CSRFProtect(app)
    app.config["IMAGE_FOLDER"] = "static/images/"
    
    # Import API routes here to avoid circular imports
    from api.users import user_bp
    app.register_blueprint(user_bp)
    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/classic')
    def classic():
        return render_template('classic.html')

    @app.route('/edit_product/<int:id>', methods=['GET', 'POST'], strict_slashes=True)
    def edit_product(id):
        """ Generate a UUID and convert it to a tring """
        cache_id = str(uuid.uuid4())
        product = Product.query.get_or_404(id)
        
        if request.method == 'POST':
            
            f = request.files['image_url']
            filename = secure_filename(f.filename)
            f.save(app.config['IMAGE_FOLDER'] + filename)

            name = request.form['name']
            image_url = filename
            price = request.form['price']
            now = datetime.datetime.now()

            product.name = name,
            product.image_url = image_url,
            product.created_at = now,
            product.price = price
            
            db.session.add(product)
            db.session.commit()
            return redirect('/products')
        else:
            return redirect('/products')
    
    @app.route('/delete_product/<int:id>', methods=['GET', 'POST'])
    def delete_product(id):
        # Remove the product by ID (replace with your actual data source)
        if request.method == 'POST':
            product = Product.query.get_or_404(id)
            db.session.delete(product)
            db.session.commit()

            # Redirect back to the product list after deleting
            return redirect('/products')
        else:
            return redirect('/products')
    @app.errorhandler(404)
    @app.route('/page_404')
    def page_404(error):
        # Get the URL that the user tried accessing
        url = request.url
        # You can customize the error page however you like
        return jsonify({'error': 'Not found', 'url': url}), 404


    @app.errorhandler(500)
    @app.route('/page_500')
    def page_500(error):
        url = request.url
        # You can customize the error page however you like
        return jsonify({'error': 'Not found', 'url': url}),  500


    @app.route('/advanced')
    def advanced():
        return render_template('advanced.html')

    @app.route('/base')
    def base():
        return render_template('base.html')

    @app.route('/blank')
    def blank():
        return render_template('blank.html')

    @app.route('/boxed')
    def boxed():
        return render_template('boxed.html')

    @app.route('/buttons')
    def buttons():
        return render_template('buttons.html')

    @app.route('/calendar')
    def calendar():
        return render_template('calendar.html')

    @app.route('/chartjs')
    def chartjs():
        return render_template('chartjs.html')


    @app.route('/collapsed-sidebar')
    def collapsed_sidebar():
        return render_template('collapsed-sidebar.html')

    @app.route('/compose')
    def compose():
        return render_template('compose.html')

    @app.route('/data')
    def data():
        return render_template('data.html')

    @app.route('/editors')
    def editors():
        return render_template('editors.html')

    @app.route('/fixed')
    def fixed():
        return render_template('fixed.html')

    @app.route('/flot')
    def flot():
        return render_template('flot.html')

    @app.route('/general')
    def general():
        return render_template('general.html')

    @app.route('/icons')
    def icons():
        return render_template('icons.html')

    @app.route('/inline')
    def inline():
        return render_template('inline.html')

    @app.route('/invoice-print')
    def invoice_print():
        return render_template('invoice-print.html')

    @app.route('/invoice')
    def invoice():
        return render_template('invoice.html')

    @app.route('/lockscreen')
    def lockscreen():
        return render_template('lockscreen.html')

    @app.route('/mailbox')
    def mailbox():
        return render_template('mailbox.html')

    @app.route('/modals')
    def modals():
        return render_template('modals.html')

    @app.route('/morris')
    def morris():
        return render_template('morris.html')

    @app.route('/read-mail')
    def read_mail():
        return render_template('read-mail.html')

    @app.route('/register')
    def register():
        return render_template('register.html')

    @app.route('/simple')
    def simple():
        return render_template('simple.html')

    @app.route('/sliders')
    def sliders():
        return render_template('sliders.html')

    @app.route('/timeline')
    def timeline():
        return render_template('timeline.html')

    @app.route('/top-nav')
    def top_nav():
        return render_template('top-nav.html')

    @app.route('/widgets')
    def widgets():
        return render_template('widgets.html')


    return app  # Return the app instance here

if __name__ == '__main__':
    app = create_app()
    # with app.app_context():
    #     db.create_all()
    app.run(port="5001", debug=True)