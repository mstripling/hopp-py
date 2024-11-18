from flask import Flask
from .routes.home import home_bp
from .routes.vendor import vendor_bp

def create_app():
    app = Flask(__name__)

    # TO DO make statard configs and load them here
    # Load configurations
    #app.config.from_object('config.Config')

    # Register blueprints (modular routes)
    app.register_blueprint(home_bp)
    app.register_blueprint(vendor_bp)
    #app.register_blueprint(auth_bp)

    return app
