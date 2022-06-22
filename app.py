from flask import Flask, render_template
import env
import os
app = Flask(__name__)

from routes.UserBlueprint import UserBlueprint

app.register_blueprint(UserBlueprint, url_prefix='/user')

@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run()