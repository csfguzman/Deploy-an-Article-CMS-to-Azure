import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'Test123$'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'pC+EHK2vCy9t6v8mXl+CtTDlnprlaFI4ejZ3FkClqjylwDjjgyMnMLH1NyTXEEIZkHVlLO+S5MRt+AStlw7c8w=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'lab1-image-storage'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sql-server-lab1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'db-lab1'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'admin1'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Test123$'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    #For Local machine
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")\
    #    or 'sqlite:///'+os.path.join(basedir, 'app.db')
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:test@localhost/cms'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "fn18Q~s5x~RK1iNp0BZ1ZbD.EFlNbpLZgDA3za4E"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "2ff24913-2e82-4823-b91f-ab329efcc6e4"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
