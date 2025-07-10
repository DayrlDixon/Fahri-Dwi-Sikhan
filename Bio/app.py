from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bio.html')  # nama file HTML kamu

if __name__ == '__main__':
    app.run(debug=True)
