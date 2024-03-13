from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'aabed9da26634fb72ea6d0e7aa62c095'


from zboxcrossvendasbebidas import route
