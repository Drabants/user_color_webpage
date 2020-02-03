from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Lets build something fun!"

if __name__ == '__main__':
    app.run()
