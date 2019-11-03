from flask import Flask

app = Flask(__name__)

# Work aroudn to circular imports
# routes needs to import app variable
# Thus app variable shadows app package

from app import routes
