from flask import Flask, redirect, url_for
from src.routes.transaction import transactiox

app = Flask(__name__, template_folder='templates')


# Blueprints
app.register_blueprint(transactiox, url_prefix='/transactions')

@app.route('/')
def index():
    return redirect(url_for('transaction.get_transactions'))
