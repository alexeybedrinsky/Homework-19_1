from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def home(path=''):
    return render_template('script.html')

if __name__ == '__main__':
    app.run(debug=True)
