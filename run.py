import sys
import os
# Add the app directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

from app import create_app

# Create the Flask app
app = create_app()

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
