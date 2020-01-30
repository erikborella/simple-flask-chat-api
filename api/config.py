DEBUG = True
SECRET_KEY = 'b60bb34c42b307171bdb88b10191d62739dd0da7e1e0c892'

# Set sqlite database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///database/db.db'

ALLOWED_EXTENSIONS = set(['png', 'jpeg', 'jpg'])
UPLOAD_FOLDER = 'public/'