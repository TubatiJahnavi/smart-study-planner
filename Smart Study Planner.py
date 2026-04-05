from app import create_app
from config import Config # Import the Config class for explicit reference

# 1. Create the application instance. This calls create_app() in app/__init__.py
# and fully initializes the app, extensions, blueprints, and database tables.
app = create_app(Config)

# 2. Start the development server
if __name__ == "__main__":
    # It is best practice to control the debug setting via the Config class, 
    # but for a simple run file, this is common.
    # Flask automatically looks up app.config['DEBUG'] if not specified here.
    # Setting debug=True here is generally only for development.
    app.run(host="127.0.0.1", port=5000, debug=True)