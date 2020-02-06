from flask import Flask, render_template, request, redirect
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods =['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        color = request.form.get('color')
        try:
            print(name)
            redis.set(name, color)
            return render_template('index.html')
        except:
            print("You messed something up")
            return render_template('index.html')
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
                return render_template('find.html', name=name, color = color)
            except:
                print('something went wrong finding %s' % (name))
                return render_template('find.html', name=name, color=None)
        else:
            return render_template('find.html', name=None)

@app.route('/delete/<name>')
def delete(name):
    redis.delete(name)
    return redirect('/find')
#I could add update name here too, but I'm leaving it just as update color
@app.route('/update/<name>', methods =['GET', 'POST'])
def update(name=None, color=None):
    if request.method == 'POST':
        color = request.form.get('color')
        redis.set(name,color)
        return render_template('update.html', name=name, color=color)
    else:
        #bug here if no name is passed in
        return  render_template('update.html', name=name, color=color)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
