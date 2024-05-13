import os

# Get the value of the FLASK_ENV environment variable
flask_env = os.environ.get('FLASK_ENV')

# Check the current environment status
if flask_env == 'development':
    print("The application is running in development mode.")
elif flask_env == 'production':
    print("The application is running in production mode.")
elif flask_env == 'testing':
    print("The application is running in testing mode.")
else:
    print("The application environment is not set or unknown.")
