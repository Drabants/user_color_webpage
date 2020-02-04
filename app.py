from flask import Flask, render_template, request, redirect
from redis import Redis

app = Flask(__name__)
redis = Redis(host='localhost', port=6379, db=0, password=None, socket_timeout=None,)

@app.route('/', methods =['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form.get('color')
        print(name)
        print(str(color))
        try:
            redis.set(name, color)
            return redirect('/')
        except:
            print("You messed something up")
            print(name)
            print(str(color))
            return redirect('/')
    else:
        return render_template('index.html')

@app.route('/find', methods =['GET', 'POST'])
def find(name=None):
    if request.method == 'POST':
        return redirect('/find')
    else:
        name = request.args.get("name")
        if name != None:
            try:
                color = redis.get(name).decode('utf-8')
                print(str(color))
                print('found %s , there favorite color is %s' %(name, color))
                return render_template('find.html', name=name)
            except:
                print('something went wrong finding %s' % (name))
                return render_template('find.html', name=name)
        else:
            return render_template('find.html', name=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
