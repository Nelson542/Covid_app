import os
from dotenv import load_dotenv

# Sets the base directory path
basedir = os.path.abspath(os.path.dirname(__file__))

# loads the environment variable file
load_dotenv()

# Function to get the environmental variables
def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected env variable '{}' not set.".format(name)
        raise Exception(message)

user = get_env_variable("POSTGRES_USER")
password = get_env_variable("POSTGRES_PASSWORD")
host = get_env_variable("POSTGRES_HOST")
database = get_env_variable("POSTGRES_DB")
port = get_env_variable("POSTGRES_PORT")

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'