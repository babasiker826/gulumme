from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gulume-ozel')
def gulume_ozel():
    return render_template('gulume-ozel.html')

if __name__ == '__main__':
    app.run(debug=True)
